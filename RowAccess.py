#! /usr/bin/python
import datetime
import json
from google.cloud import bigquery
from re import search

'''*********
Apply row level security based on access list input
*********'''
#Setup variables
T=[]

date=datetime.datetime.now()
monthValue=int(date.strftime("%m"))
monthValue-=1
metricsDate="{}-{}-{}".format(date.strftime("%Y"),monthValue,"01")
#Change GCPDate for testing
GCPDate="{}-{}-{}".format(date.strftime("%Y"),date.strftime("%m"),"01")
project_id="<projectid>"
dataset="<dataset>"
tableAccessList="<tablewithaccesslist>"

dataSource=bigquery.Client(project=project_id)

print("Executing for date :{}".format(metricsDate))

metaQuery='Select * from `{}.{}.{}`'.format(project_id,dataset,tableAccessList)

job=dataSource.query(metaQuery)
result=job.result()

for row in result:
    project=row[1]
    dataSet=row[2]
    table=row[3]
    policyName=row[4]
    groupList=None if row[5] is None else row[5].split(",")
    usersList=None if row[7] is None else row[7].split(",")
    access=row[8]
    tempList=[]
    print("Extracting access list:-project:{} dataSet:{} table:{} groups:{}  users:{} access:{}"
    .format(project,dataSet,table,groupList,usersList,access))
    
    #Reading metadata

    sqlQuery = "CREATE OR REPLACE ROW ACCESS POLICY {} ON `{}.{}.{}` GRANT TO".format(policyName,project,dataSet,table)
    usersText=""
    if(groupList != None and len(groupList)>=1):
        for groupName in groupList:
            usersText+=""""group:{}",""".format(groupName)

            

    if(usersList != None and len(usersList)>=1):
        sqlQuery = "CREATE OR REPLACE ROW ACCESS POLICY {} ON `{}.{}.{}` GRANT TO".format(policyName,project,dataSet,table)
        for usersName in usersList:
            usersText+=""""user:{}",""".format(usersName)
               
    usersText=usersText[:-1]
    sqlQuery+="""({}) FILTER USING({})""".format(usersText,access) 
    print(sqlQuery)       

    job=dataSource.query(sqlQuery)
    job.result()
