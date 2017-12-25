import subprocess, sys, os, time;
import jenkinsapi

from jenkinsapi.jenkins import Jenkins

process = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE)

TowerIP = ["210.114.90.167:2375"]

command2 = "docker ps"

print command2

out = subprocess.check_output(command2, shell=True)
print out

#server = jenkins.Jenkins('http://203.237.53.137:8080', username='chorwon', password='ff80e94dbe84b0a98dc8976407102f14')
#user = server.get_whoami()
#version = server.get_version()

#print('Hello %s from Jenkins %s' % (user['fullname'], version))

J = Jenkins('http://localhost:8080', username='chorwon', password='ff80e94dbe84b0a98dc8976407102f14')
print(J.version)

job1 = J['IoT Deploy Job']
job2 = J['Flafka_S2']

print(job1.get_description())
print(job1.get_scm_url())

build_job1 = job1.get_last_completed_build()
print(build_job1)
print(build_job1.is_running())
print(build_job1.get_revision())
print(build_job1.get_status())

build_job2 = job2.get_last_completed_build()
print(build_job2)
print(build_job2.get_status())
print(build_job2.is_running())
print(build_job2.get_status())
