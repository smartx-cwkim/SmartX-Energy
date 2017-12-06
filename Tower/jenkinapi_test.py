import subprocess, sys, os, time;
import jenkinsapi

from jenkinsapi.jenkins import Jenkins

process = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE)

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

job = J['IoT Deploy Job']

print(job.get_description())
print(job.get_scm_url())

build = job.get_last_completed_build()
print(build)
print(build.is_running())
print(build.get_revision())
print(build.get_status())



