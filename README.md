# code-20220918-navaneethanramasamy
Python based BMI Calculator

### Description

This application focuses on calculatiing bmi of the passed json data and followed by generating the observations about the health category from the calculated bmi value.

preset of observation logics are added already.

### How to Run:

#### Running via Docker Container:
`docker-compose up`

#### Run without Docker Container:

Python version: 3.10.4

` python bmi.py --jsonFile=./input.json`

> bmi.py -> filename   
> jsonFile -> contains json data   
> input.json -> example json file   

#### Sample console output from docker run
<pre><font color="#586E75"><b>navatux@navatux-ThinkPad-L460</b></font>:<font color="#839496"><b>~/work/code-20220918-navaneethanramasamy</b></font>$ docker-compose up
<font color="#B58900">WARNING</font>: Found orphan containers (code-20220918-navaneethanramasamy_bmi_1) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up.
Building mybmi
Sending build context to Docker daemon  130.6kB
Step 1/4 : FROM python:3.9-slim
 ---&gt; 2de9c79b2c75
Step 2/4 : WORKDIR /bmi
 ---&gt; Using cache
 ---&gt; 81fef9b7d220
Step 3/4 : COPY . .
 ---&gt; 34dd592dbb9a
Step 4/4 : CMD [ &quot;python&quot;, &quot;bmi.py&quot; , &quot;--jsonFile&quot;, &quot;./input.json&quot;]
 ---&gt; Running in bf422e4b93c7
Removing intermediate container bf422e4b93c7
 ---&gt; c68e698ab057
Successfully built c68e698ab057
Successfully tagged code-20220918-navaneethanramasamy_mybmi:latest
<font color="#B58900">WARNING</font>: Image for service mybmi was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Creating code-20220918-navaneethanramasamy_mybmi_1 ... <font color="#859900">done</font>
Attaching to code-20220918-navaneethanramasamy_mybmi_1
<font color="#2AA198">mybmi_1  |</font> Count of Overweight Observations:  2
<font color="#2AA198">mybmi_1  |</font> Count of Overweight Observations and Female Gender:  2
<font color="#2AA198">mybmi_1  |</font> Count of Very High Risk persons:  0
<font color="#2AA198">code-20220918-navaneethanramasamy_mybmi_1 exited with code 0</font>
<font color="#586E75"><b>navatux@navatux-ThinkPad-L460</b></font>:<font color="#839496"><b>~/work/code-20220918-navaneethanramasamy</b></font>$ 
</pre>

### Test:

Unit tests added in `test_bmi.py`

### Author:
Navaneethan <nava.nmr@gmail.com>

### Purpose:
Interview problem
