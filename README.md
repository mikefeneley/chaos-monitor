# chaos-monitor
This is a placeholder repo. No significant work has been done on this project yet.

<b>Roadmap</b>

This repo will be used to create an integrity checking tool. We want to verify that important, static systems files remain unchanged. So this tool will create checksums of these files and store them on a remote database server. It then periodically recalculates the checksums of said files and compares them to the stored checksum values. If they are the same, the system integrity has been verified. If not, then the file has been changed either maliciously or not and the cause should be investigated.

<b>Dependencies</b>

MySQL Database<br>
MySQL Python Connectors<br>
PyDaemon<br>
validate_email<br>

<b>Dependency Install</b>

pip install pydaemon <br>
pip install validate_email<br>
sudo pip install pydns==2.3.6<br>

<br>
<br>
<b>Contact:</b>
<ul>
<li>Michael Feneley: mfeneley(at)vt.edu</li>
<li>Anshul Basia: anshul7(at)vt.edu</li>
</ul>
