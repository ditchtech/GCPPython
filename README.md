# GCPPython
The file reads setup data from BigQuery table, which can be updated for feeding inputs to the script.</br>

<p><u>BQ Codes -</u></p>

<p>DROP ALL ROW ACCESS POLICIES ON `projectid.TestData.international_debt`;</p>

<p>CREATE OR REPLACE ROW ACCESS POLICY Apac_Policy_Group<br />
ON `projectid.TestData.international_debt`<br />
GRANT TO(&quot;group:testaccessgroup@googlegroups.com&quot;)&nbsp;<br />
FILTER USING(TRUE);</p>

<p>CREATE OR REPLACE ROW ACCESS POLICY Apac_Policy<br />
ON `projectid.TestData.international_debt`<br />
GRANT TO(&quot;user:xxxxxx@gmail.com&quot;)&nbsp;<br />
FILTER USING(&lt;Condition&gt;);</p>

Youtube Tutorial - <a href="https://youtu.be/c0dLYkygiKg" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/youtube.svg" alt="uc9dvp2ld1zbajymnpr7netg" height="30" width="40" /></a>

Table schema for data entry should be as follows - </br>
<table cellspacing="0" style="border-collapse:collapse; width:192px">
	<tbody>
		<tr>
			<td style="background-color:white; border-bottom:1px solid #e0e0e0; border-left:none; border-right:none; border-top:none; height:20px; text-align:center; vertical-align:top; white-space:nowrap; width:64px"><span style="font-size:9px"><span style="color:#707070"><span style="font-family:inherit">Field name</span></span></span></td>
			<td style="background-color:white; border-bottom:1px solid #e0e0e0; border-left:none; border-right:none; border-top:none; text-align:center; vertical-align:top; white-space:nowrap; width:64px"><span style="font-size:9px"><span style="color:#707070"><span style="font-family:inherit">Type</span></span></span></td>
			<td style="background-color:white; border-bottom:1px solid #e0e0e0; border-left:none; border-right:none; border-top:none; text-align:center; vertical-align:top; white-space:nowrap; width:64px"><span style="font-size:9px"><span style="color:#707070"><span style="font-family:inherit">Mode</span></span></span></td>
		</tr>
		<tr>
			<td style="background-color:white; border-bottom:1px solid #e0e0e0; border-left:none; border-right:none; border-top:none; height:28px; text-align:left; vertical-align:middle; white-space:nowrap">
			<p><span style="font-size:11px"><span style="color:rgba(0, 0, 0, 0.66)"><span style="font-family:inherit">Project</span></span></span></p>
			</td>
			<td style="background-color:white; border-bottom:1px solid #e0e0e0; border-left:none; border-right:none; border-top:none; text-align:left; vertical-align:top; white-space:normal; width:64px"><span style="font-size:11px"><span style="color:rgba(0, 0, 0, 0.66)"><span style="font-family:inherit">STRING</span></span></span></td>
			<td style="background-color:white; border-bottom:1px solid #e0e0e0; border-left:none; border-right:none; border-top:none; text-align:left; vertical-align:top; white-space:normal; width:64px"><span style="font-size:11px"><span style="color:rgba(0, 0, 0, 0.66)"><span style="font-family:inherit">NULLABLE</span></span></span></td>
		</tr>
		<tr>
			<td style="background-color:white; border-bottom:1px solid #e0e0e0; border-left:none; border-right:none; border-top:none; height:28px; text-align:left; vertical-align:middle; white-space:nowrap">
			<p><span style="font-size:11px"><span style="color:rgba(0, 0, 0, 0.66)"><span style="font-family:inherit">Dataset</span></span></span></p>
			</td>
			<td style="background-color:white; border-bottom:1px solid #e0e0e0; border-left:none; border-right:none; border-top:none; text-align:left; vertical-align:top; white-space:normal; width:64px"><span style="font-size:11px"><span style="color:rgba(0, 0, 0, 0.66)"><span style="font-family:inherit">STRING</span></span></span></td>
			<td style="background-color:white; border-bottom:1px solid #e0e0e0; border-left:none; border-right:none; border-top:none; text-align:left; vertical-align:top; white-space:normal; width:64px"><span style="font-size:11px"><span style="color:rgba(0, 0, 0, 0.66)"><span style="font-family:inherit">NULLABLE</span></span></span></td>
		</tr>
		<tr>
			<td style="background-color:white; border-bottom:1px solid #e0e0e0; border-left:none; border-right:none; border-top:none; height:28px; text-align:left; vertical-align:middle; white-space:nowrap">
			<p><span style="font-size:11px"><span style="color:rgba(0, 0, 0, 0.66)"><span style="font-family:inherit">Table</span></span></span></p>
			</td>
			<td style="background-color:white; border-bottom:1px solid #e0e0e0; border-left:none; border-right:none; border-top:none; text-align:left; vertical-align:top; white-space:normal; width:64px"><span style="font-size:11px"><span style="color:rgba(0, 0, 0, 0.66)"><span style="font-family:inherit">STRING</span></span></span></td>
			<td style="background-color:white; border-bottom:1px solid #e0e0e0; border-left:none; border-right:none; border-top:none; text-align:left; vertical-align:top; white-space:normal; width:64px"><span style="font-size:11px"><span style="color:rgba(0, 0, 0, 0.66)"><span style="font-family:inherit">NULLABLE</span></span></span></td>
		</tr>
		<tr>
			<td style="background-color:white; border-bottom:1px solid #e0e0e0; border-left:none; border-right:none; border-top:none; height:28px; text-align:left; vertical-align:middle; white-space:nowrap">
			<p><span style="font-size:11px"><span style="color:rgba(0, 0, 0, 0.66)"><span style="font-family:inherit">PolicyName</span></span></span></p>
			</td>
			<td style="background-color:white; border-bottom:1px solid #e0e0e0; border-left:none; border-right:none; border-top:none; text-align:left; vertical-align:top; white-space:normal; width:64px"><span style="font-size:11px"><span style="color:rgba(0, 0, 0, 0.66)"><span style="font-family:inherit">STRING</span></span></span></td>
			<td style="background-color:white; border-bottom:1px solid #e0e0e0; border-left:none; border-right:none; border-top:none; text-align:left; vertical-align:top; white-space:normal; width:64px"><span style="font-size:11px"><span style="color:rgba(0, 0, 0, 0.66)"><span style="font-family:inherit">NULLABLE</span></span></span></td>
		</tr>
		<tr>
			<td style="background-color:white; border-bottom:1px solid #e0e0e0; border-left:none; border-right:none; border-top:none; height:28px; text-align:left; vertical-align:middle; white-space:nowrap">
			<p><span style="font-size:11px"><span style="color:rgba(0, 0, 0, 0.66)"><span style="font-family:inherit">Groups</span></span></span></p>
			</td>
			<td style="background-color:white; border-bottom:1px solid #e0e0e0; border-left:none; border-right:none; border-top:none; text-align:left; vertical-align:top; white-space:normal; width:64px"><span style="font-size:11px"><span style="color:rgba(0, 0, 0, 0.66)"><span style="font-family:inherit">STRING</span></span></span></td>
			<td style="background-color:white; border-bottom:1px solid #e0e0e0; border-left:none; border-right:none; border-top:none; text-align:left; vertical-align:top; white-space:normal; width:64px"><span style="font-size:11px"><span style="color:rgba(0, 0, 0, 0.66)"><span style="font-family:inherit">NULLABLE</span></span></span></td>
		</tr>
		<tr>
			<td style="background-color:white; border-bottom:1px solid #e0e0e0; border-left:none; border-right:none; border-top:none; height:28px; text-align:left; vertical-align:middle; white-space:nowrap">
			<p><span style="font-size:11px"><span style="color:rgba(0, 0, 0, 0.66)"><span style="font-family:inherit">Admin</span></span></span></p>
			</td>
			<td style="background-color:white; border-bottom:1px solid #e0e0e0; border-left:none; border-right:none; border-top:none; text-align:left; vertical-align:top; white-space:normal; width:64px"><span style="font-size:11px"><span style="color:rgba(0, 0, 0, 0.66)"><span style="font-family:inherit">STRING</span></span></span></td>
			<td style="background-color:white; border-bottom:1px solid #e0e0e0; border-left:none; border-right:none; border-top:none; text-align:left; vertical-align:top; white-space:normal; width:64px"><span style="font-size:11px"><span style="color:rgba(0, 0, 0, 0.66)"><span style="font-family:inherit">NULLABLE</span></span></span></td>
		</tr>
		<tr>
			<td style="background-color:white; border-bottom:1px solid #e0e0e0; border-left:none; border-right:none; border-top:none; height:28px; text-align:left; vertical-align:middle; white-space:nowrap">
			<p><span style="font-size:11px"><span style="color:rgba(0, 0, 0, 0.66)"><span style="font-family:inherit">Users</span></span></span></p>
			</td>
			<td style="background-color:white; border-bottom:1px solid #e0e0e0; border-left:none; border-right:none; border-top:none; text-align:left; vertical-align:top; white-space:normal; width:64px"><span style="font-size:11px"><span style="color:rgba(0, 0, 0, 0.66)"><span style="font-family:inherit">STRING</span></span></span></td>
			<td style="background-color:white; border-bottom:1px solid #e0e0e0; border-left:none; border-right:none; border-top:none; text-align:left; vertical-align:top; white-space:normal; width:64px"><span style="font-size:11px"><span style="color:rgba(0, 0, 0, 0.66)"><span style="font-family:inherit">NULLABLE</span></span></span></td>
		</tr>
		<tr>
			<td style="background-color:white; border-bottom:1px solid #e0e0e0; border-left:none; border-right:none; border-top:none; height:28px; text-align:left; vertical-align:middle; white-space:nowrap">
			<p><span style="font-size:11px"><span style="color:rgba(0, 0, 0, 0.66)"><span style="font-family:inherit">AccessCondition</span></span></span></p>
			</td>
			<td style="background-color:white; border-bottom:1px solid #e0e0e0; border-left:none; border-right:none; border-top:none; text-align:left; vertical-align:top; white-space:normal; width:64px"><span style="font-size:11px"><span style="color:rgba(0, 0, 0, 0.66)"><span style="font-family:inherit">STRING</span></span></span></td>
			<td style="background-color:white; border-bottom:1px solid #e0e0e0; border-left:none; border-right:none; border-top:none; text-align:left; vertical-align:top; white-space:normal; width:64px"><span style="font-size:11px"><span style="color:rgba(0, 0, 0, 0.66)"><span style="font-family:inherit">NULLABLE</span></span></span></td>
		</tr>
	</tbody>
</table>

</br>
Note, admin functionality has not been implemented and can be left out blank.</br>
<p>&nbsp;</p>

<p>Multiple user/group entry in table should be of format :user1@gmail.com,user2@gmail.com</p>

<p>Access permissions should be of format identical to where clause :country_name in (&#39;Sri Lanka&#39;,&#39;Vietnam&#39;,&#39;China&#39;,&#39;Hong Kong&#39;,&#39;Indonesia&#39;,&#39;India&#39;)</p>

<h3 align="left">Connect with me:</h3>
<a href="https://linkedin.com/in/anthonygomescal" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="anthonygomescal" height="30" width="40" /></a>
<a href="https://stackoverflow.com/users/raptorx" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/stack-overflow.svg" alt="raptorx" height="30" width="40" /></a>
<a href="https://www.hackerrank.com/raptorx" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/hackerrank.svg" alt="raptorx" height="30" width="40" /></a>
<a href="https://www.youtube.com/channel/UC9DVP2Ld1ZBajymnpr7NEtg" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/youtube.svg" alt="uc9dvp2ld1zbajymnpr7netg" height="30" width="40" /></a>

