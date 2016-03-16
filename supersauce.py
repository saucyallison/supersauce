#!/usr/bin/env python
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   ----------------
#
#   Sauce Labs REST API documentation:
#     http://saucelabs.com/docs/rest

import base64
import sys
import json
import os
import time

is_py2 = sys.version_info.major is 2

if is_py2:
    import httplib as http_client
else:
    import httpclient as http_client

DEFAULT_USER = os.environ.get('SAUCE_USERNAME')

def make_headers():
    base64string = get_encoded_auth_string()
    headers = {
        'Authorization': 'Basic %s' % base64string,
        'Content-Type': 'application/json',
    }
    return headers

def request(method, url, body=None):
    connection = http_client.HTTPSConnection('saucelabs.com')
    connection.request(method, url, body, headers=make_headers())
    response = connection.getresponse()
    json_data = response.read()
    connection.close()
    if response.status != 200:
        raise Exception('%s: %s.\nSauce Status NOT OK' %
                        (response.status, response.reason))
    return json_data

def get_encoded_auth_string():
    auth_info = '%s:%s' % (os.environ['SAUCE_USERNAME'], os.environ['SAUCE_ACCESS_KEY'])
    if is_py2:
        base64string = base64.encodestring(auth_info)[:-1]
    else:
        base64string = base64.b64encode(auth_info.encode(encoding='UTF-8')).decode(encoding='UTF-8')
    return base64string

def get_job_ids(limit=None):
    """
        List recent jobs id's belonging to the user (up to `limit`).

        ex: supersauce.get_job_ids(3)
            supersauce.jobids(3)

        >>> ['f74ea0fa26a24f0296866624dcc648fb', 'ecfa42b873e9466da1bc18da2b10f950', 'c23f7e304a2643eda5e5aea6189420e1']
    """
    method = 'GET'
    limit_str = '?limit='+str(limit) if limit else ''
    url = '/rest/v1/%s/jobs%s' % (os.environ['SAUCE_USERNAME'], limit_str)
    json_data = request(method, url)
    jobs = json.loads(json_data)
    job_ids = [attr['id'] for attr in jobs]
    return job_ids
def jobids(limit=None):
    return get_job_ids(limit)

def get_jobs(user=DEFAULT_USER):
    """
        Gets full info for latest 100 jobs belonging to `user` (defaults to SAUCE_USERNAME).

        ex: supersauce.get_jobs('awilbur')
            supersauce.getjobs('awilbur')
            supersauce.jobs('awilbur')

        >>> [{'browser_short_version': '9', 'video_url': 'https://saucelabs.com/jobs/f74ea0fa26a24f0296866624dcc648fb/video.flv', 'creation_time': 1458104287, 'custom-data': None, 'browser_version': '9.0.', 'owner': 'awilbur', 'id': 'f74ea0fa26a24f0296866624dcc648fb', 'record_screenshots': True, 'record_video': True, 'build': None, 'passed': None, 'public': None, 'assigned_tunnel_id': None, 'status': 'complete', 'log_url': 'https://saucelabs.com/jobs/f74ea0fa26a24f0296866624dcc648fb/selenium-server.log', 'start_time': 1458104287, 'proxied': False, 'modification_time': 1458104378, 'tags': [], 'consolidated_status': 'complete', 'commands_not_successful': 1, 'name': None, 'end_time': 1458104378, 'error': None, 'os': 'Mac 10.11', 'breakpointed': None, 'browser': 'safari'},
            ... (x99)
            ]
    """
    method = 'GET'
    url = '/rest/v1/%s/jobs?full=true' % user
    json_data = request(method, url)
    jobs = json.loads(json_data)
    return jobs
def getjobs(user=DEFAULT_USER):
    return get_jobs(user)
def jobs(user=DEFAULT_USER):
    return get_jobs(user)

def get_job(user, jobid):
    """
        Get a single job's full info for `user`'s job with id `jobid`.

        ex: supersauce.get_job('awilbur', 'f74ea0fa26a24f0296866624dcc648fb')
            supersauce.getjob('awilbur', 'f74ea0fa26a24f0296866624dcc648fb')

        >>> {'browser_short_version': '9', 'video_url': 'https://saucelabs.com/jobs/f74ea0fa26a24f0296866624dcc648fb/video.flv', 'creation_time': 1458104287, 'custom-data': None, 'browser_version': '9.0.', 'owner': 'awilbur', 'automation_backend': 'webdriver', 'id': 'f74ea0fa26a24f0296866624dcc648fb', 'collects_automator_log': False, 'record_screenshots': True, 'record_video': True, 'build': None, 'passed': None, 'public': None, 'end_time': 1458104378, 'status': 'complete', 'log_url': 'https://saucelabs.com/jobs/f74ea0fa26a24f0296866624dcc648fb/selenium-server.log', 'start_time': 1458104287, 'proxied': False, 'modification_time': 1458104378, 'tags': [], 'consolidated_status': 'complete', 'commands_not_successful': 1, 'name': None, 'selenium_version': '2.48.0', 'manual': False, 'assigned_tunnel_id': None, 'error': None, 'os': 'Mac 10.11', 'breakpointed': None, 'browser': 'safari'}
    """
    method = 'GET'
    url = '/rest/v1/%s/jobs/%s' % (user, jobid)
    try:
        json_data = request(method, url)
        # sometimes things don't work, because internet. try again
    except:
        try:
            print '    getjob() failed, trying again (%s)' % (jobid)
            time.sleep(1)
            json_data = request(method, url)
        except:
            print '    getjob() failed twice (%s)' % (jobid)
    json_result = json.loads(json_data)
    return json_result
def getjob(user, jobid):
    return get_job(user, jobid)

def jobsfrom(user, fromtime):
    """
        List all of `user`'s jobs since the unix timestamp `fromtime`.

        ex: supersauce.jobsfrom('awilbur', 1458101920)

        >>> [{'id': 'f74ea0fa26a24f0296866624dcc648fb'}, {'id': 'ecfa42b873e9466da1bc18da2b10f950'}, {'id': 'c23f7e304a2643eda5e5aea6189420e1'}, {'id': 'c03e8bb16fc54fddb7c521ab72d49d38'}, {'id': 'bee47807422d4c8796f581017efc1fb5'}, {'id': 'be73bef773b144e08644c3453b171110'}]
    """
    method = 'GET'
    url = '/rest/v1/%s/jobs?from=%s' % (user, fromtime)
    json_data = request(method, url)
    jobs = json.loads(json_data)
    return jobs

def jobsfromto(user, fromtime, totime):
    """
        List all of `user`'s jobs in the range of unix timestamps `fromtime` until `totime`.

        ex: supersauce.jobsfromto('awilbur', 1458101620, 1458101920)

        >>> [{'id': 'e40108a6081e419b83797f748d66eeba'}, {'id': 'e18ed89b49754074bdfd64af492bf062'}, {'id': 'bf75c08a93164ffa9e661a4839ead3ea'}, {'id': '90ddefddafa44f5ba1ac649a99321007'}, {'id': '8bbf842ab3654a7bb63bbc71c22240cc'}, {'id': '7e8886ab496b4d568f5fdd0fdd6e96a4'}, {'id': '75ac5bb424fe40c7a4b5ec2aef505690'}, {'id': '50cab4505b4c4ab08fc4b8631069789d'}, {'id': '2f3c6635767a4ad9824935ad579054c0'}, {'id': '2628e61ed13a411eae36db11be659afc'}]
    """
    method = 'GET'
    url = '/rest/v1/%s/jobs?from=%s&to=%s' % (user, fromtime, totime)
    json_data = request(method, url)
    jobs = json.loads(json_data)
    return jobs

def latest(user=DEFAULT_USER):
    """
        Get full info `user`'s latest (single) job.

        ex: supersauce.latest('awilbur')

        >>> {'browser_short_version': '9', 'video_url': 'https://saucelabs.com/jobs/f74ea0fa26a24f0296866624dcc648fb/video.flv', 'creation_time': 1458104287, 'custom-data': None, 'browser_version': '9.0.', 'owner': 'awilbur', 'automation_backend': 'webdriver', 'id': 'f74ea0fa26a24f0296866624dcc648fb', 'collects_automator_log': False, 'record_screenshots': True, 'record_video': True, 'build': None, 'passed': None, 'public': None, 'end_time': 1458104378, 'status': 'complete', 'log_url': 'https://saucelabs.com/jobs/f74ea0fa26a24f0296866624dcc648fb/selenium-server.log', 'start_time': 1458104287, 'proxied': False, 'modification_time': 1458104378, 'tags': [], 'consolidated_status': 'complete', 'commands_not_successful': 1, 'name': None, 'selenium_version': '2.48.0', 'manual': False, 'assigned_tunnel_id': None, 'error': None, 'os': 'Mac 10.11', 'breakpointed': None, 'browser': 'safari'}
    """
    method = 'GET'
    url = '/rest/v1/%s/jobs?limit=1' % (user)
    json_data = request(method, url)
    jobs = json.loads(json_data)
    job = jobs[0]['id'] or ''
    return getjob(user, job)

def update_name(jobid, newname):
    """
        Update your job `jobid` (or 'latest'/'L'/'l') to `newname`.

        ex: supersauce.updatename('f74ea0fa26a24f0296866624dcc648fb', 'much better name')

        >>> {'browser_short_version': '9', 'video_url': 'https://saucelabs.com/jobs/f74ea0fa26a24f0296866624dcc648fb/video.flv', 'creation_time': 1458104287, 'custom-data': None, 'browser_version': '9.0.', 'owner': 'awilbur', 'id': 'f74ea0fa26a24f0296866624dcc648fb', 'record_screenshots': True, 'record_video': True, 'build': None, 'passed': None, 'public': None, 'end_time': 1458104378, 'status': 'complete', 'log_url': 'https://saucelabs.com/jobs/f74ea0fa26a24f0296866624dcc648fb/selenium-server.log', 'start_time': 1458104287, 'proxied': False, 'modification_time': 1458146404, 'tags': [], 'consolidated_status': 'complete', 'commands_not_successful': 1, 'name': 'much better name', 'assigned_tunnel_id': None, 'error': None, 'os': 'Mac 10.11', 'breakpointed': None, 'browser': 'safari'}
    """
    job = jobid
    if jobid in ['latest', 'l', 'L']:
        job = latest()['id']
    update_info = {'name': newname}
    body = json.dumps(update_info)
    method = 'PUT'
    url = '/rest/v1/%s/jobs/%s' % (os.environ['SAUCE_USERNAME'], job)
    json_data = request(method, url, body=body)
    attributes = json.loads(json_data)
    return attributes
def updatename(jobid, newname):
    return update_name(jobid, newname)

def update_job(job_id, build_num=None, custom_data=None,
               name=None, passed=None, public=None, tags=None):
    """
        Update attributes for the specified job.

        Options:
            name
            build_num
            passed
            public
            tags
            custom_data

        ex: supersauce.update_job('f74ea0fa26a24f0296866624dcc648fb', build_num='newbuild', passed=True)

        >>> {'browser_short_version': '9', 'video_url': 'https://saucelabs.com/jobs/f74ea0fa26a24f0296866624dcc648fb/video.flv', 'creation_time': 1458104287, 'custom-data': None, 'browser_version': '9.0.', 'owner': 'awilbur', 'id': 'f74ea0fa26a24f0296866624dcc648fb', 'record_screenshots': True, 'record_video': True, 'build': 'newbuild', 'passed': True, 'public': None, 'end_time': 1458104378, 'status': 'complete', 'log_url': 'https://saucelabs.com/jobs/f74ea0fa26a24f0296866624dcc648fb/selenium-server.log', 'start_time': 1458104287, 'proxied': False, 'modification_time': 1458150018, 'tags': [], 'consolidated_status': 'passed', 'commands_not_successful': 1, 'name': 'much better name', 'assigned_tunnel_id': None, 'error': None, 'os': 'Mac 10.11', 'breakpointed': None, 'browser': 'safari'}
    """
    content = {}
    if build_num is not None:
        content['build'] = build_num
    if custom_data is not None:
        content['custom-data'] = custom_data
    if name is not None:
        content['name'] = name
    if passed is not None:
        content['passed'] = passed
    if public is not None:
        content['public'] = public
    if tags is not None:
        content['tags'] = tags
    body = json.dumps(content)
    method = 'PUT'
    url = '/rest/v1/%s/jobs/%s' % (os.environ['SAUCE_USERNAME'], job_id)
    json_data = request(method, url, body=body)
    attributes = json.loads(json_data)
    return attributes

def gettun(tunnelid):
    """
        List all of `user`'s jobs in the range of unix timestamps `fromtime` until `totime`.

        ex: supersauce.jobsfromto('awilbur', 1458101620, 1458101920)

        >>> [{'id': 'e40108a6081e419b83797f748d66eeba'}, {'id': 'e18ed89b49754074bdfd64af492bf062'}, {'id': 'bf75c08a93164ffa9e661a4839ead3ea'}, {'id': '90ddefddafa44f5ba1ac649a99321007'}, {'id': '8bbf842ab3654a7bb63bbc71c22240cc'}, {'id': '7e8886ab496b4d568f5fdd0fdd6e96a4'}, {'id': '75ac5bb424fe40c7a4b5ec2aef505690'}, {'id': '50cab4505b4c4ab08fc4b8631069789d'}, {'id': '2f3c6635767a4ad9824935ad579054c0'}, {'id': '2628e61ed13a411eae36db11be659afc'}]
    """
    method = 'GET'
    url = '/rest/v1/%s/tunnels/%s' % (os.environ['SAUCE_USERNAME'], tunnelid)
    json_data = request(method, url)
    attributes = json.loads(json_data)
    return attributes

def get_tunnels(user=DEFAULT_USER):
    """
        List all active tunnels from `user`.

        ex: supersauce.get_tunnels('awilbur')
            supersauce.gettuns('awilbur')
            supersauce.tunnels('awilbur')
            supersauce.tuns('awilbur')

        >>> ['11f0171429904a2dbd84d36ad0e8c171']
    """
    method = 'GET'
    url = '/rest/v1/%s/tunnels' % user
    json_data = request(method, url)
    attributes = json.loads(json_data)
    return attributes
def gettuns(user=DEFAULT_USER):
    return get_tunnels(user)
def tunnels(user=DEFAULT_USER):
    return gettuns(user)
def tuns(user=DEFAULT_USER):
    return get_tunnels(user)

def activity(user=DEFAULT_USER):
    """
        Calls the activity endpoint for `user`, displaying real-time concurrency usage for all subaccounts.

        ex: supersauce.activity('awilbur')

        >>> {'subaccounts': {'awilbursub2': {'in progress': 0, 'all': 0, 'queued': 0}, 'awilbursub': {'in progress': 0, 'all': 0, 'queued': 0}, 'TrueBlue': {'in progress': 0, 'all': 0, 'queued': 0}, 'BigRed': {'in progress': 0, 'all': 0, 'queued': 0}, 'YOUR_USERNAME': {'in progress': 0, 'all': 0, 'queued': 0}, 'awilbur_sub': {'in progress': 0, 'all': 0, 'queued': 0}, 'demo-user': {'in progress': 0, 'all': 0, 'queued': 0}, 'awilbur': {'in progress': 0, 'all': 0, 'queued': 0}, 'TrueBlue2': {'in progress': 0, 'all': 0, 'queued': 0}}, 'totals': {'in progress': 0, 'all': 0, 'queued': 0}}
    """
    method = 'GET'
    url = '/rest/v1/%s/activity' % user
    json_data = request(method, url)
    json_result = json.loads(json_data)
    return json_result

def get_subaccounts(user=DEFAULT_USER):
    """
        Calls the activity endpoint for `user`, displaying real-time concurrency usage for all subaccounts.

        ex: supersauce.get_subs('awilbur')
            supersauce.getsubs('awilbur')
            supersauce.subaccounts('awilbur')
            supersauce.subs('awilbur')

        >>> ['BigRed', 'demo-user', 'TrueBlue', 'awilbursub2', 'YOUR_USERNAME', 'awilbur_sub', 'awilbursub', 'TrueBlue2']
    """
    return [sub for sub in activity(user)['subaccounts'].keys() if sub != user]
def subs(user=DEFAULT_USER):
    return get_subaccounts(user)
def get_subs(user=DEFAULT_USER):
    return get_subaccounts(user)
def getsubs(user=DEFAULT_USER):
    return get_subaccounts(user)
def subaccounts(user=DEFAULT_USER):
    return get_subaccounts(user)

def get_account_details(user=DEFAULT_USER):
    """
        Returns account information for `user`.

        ex: supersauce.get_account_details('awilbur')

        >>> {'domain': None, 'last_name': None, 'creation_time': 1398107526, 'user_type': 'admin', 'concurrency_limit': {'mac': 100, 'scout': 100, 'overall': 100, 'real_device': 30}, 'manual_minutes': 'infinite', 'can_run_manual': True, 'prevent_emails': ['marketing'], 'id': 'awilbur', 'first_name': None, 'verified': True, 'subscribed': False, 'title': None, 'ancestor_allows_subaccounts': True, 'ancestor': 'awilbur', 'email': 'allison@saucelabs.com', 'username': 'awilbur', 'access_key': '4b7b6bcc-1a60-41a4-b98e-cce10ac12ada', 'parent': None, 'is_admin': None, 'is_public': False, 'vm_lockdown': False, 'name': 'Allison Wilbur', 'is_sso': False, 'entity_type': 'individual', 'ancestor_concurrency_limit': {'mac': 100, 'scout': 100, 'overall': 100, 'real_device': 30}, 'minutes': 'infinite'}
    """
    method = 'GET'
    url = '/rest/v1/users/%s' % user
    json_data = request(method, url)
    attributes = json.loads(json_data)
    return attributes

def get_status():
    """
        Access the current status of Sauce Labs' services.

        ex: supersauce.get_status()

        >>> {'wait_time': 3.6167102966841185, 'service_operational': True, 'status_message': 'Basic service status checks passed.'}
    """
    method = 'GET'
    url = '/rest/v1/info/status'
    json_data = request(method, url)
    status = json.loads(json_data)
    return status

def get_browsers(type='webdriver'):
    """
        Get list of all browsers currently supported on Sauce Labs.
        `type` defaults to 'webdriver'. ('appium' and 'all' are also supported.

        ex: supersauce.get_browsers()

        >>> [{'short_version': '7.0', 'long_name': 'iPad', 'api_name': 'ipad', 'long_version': '7.0.', 'device': 'ipad', 'latest_stable_version': '', 'automation_backend': 'webdriver', 'os': 'Mac 10.9'}, {'short_version': '7.1', ...
            ...
            ]
    """
    method = 'GET'
    url = '/rest/v1/info/platforms/%s' % type
    json_data = request(method, url)
    browsers = json.loads(json_data)
    return browsers

def get_historical_usage(user=DEFAULT_USER):
    """
        Access historical account usage.

        ex: supersauce.get_historical_usage()

        >>> {'usage': [['2016-1-20', [2, 24]], ['2016-1-21', [5, 1185]], ['2016-1-22', [245, 44507]], ['2016-1-23', [100, 8197]], ['2016-1-25', [3, 482]], ['2016-1-26', [1, 14]], ['2016-1-27', [100, 8904]], ['2016-2-4', [6, 296]], ['2016-2-5', [2, 26]], ['2016-2-9', [1, 53]], ['2016-2-10', [1, 64]], ['2016-2-11', [4, 219]], ['2016-2-12', [24, 13910]], ['2016-2-13', [330, 31796]], ['2016-2-16', [2, 21]], ['2016-2-17', [404, 15329]], ['2016-2-18', [2, 4622]], ['2016-2-19', [4, 3337]], ['2016-2-24', [1, 33]], ['2016-2-25', [512, 144174]], ['2016-2-26', [3, 479]], ['2016-2-27', [1, 5622]], ['2016-3-1', [4, 911]], ['2016-3-3', [4, 1452]], ['2016-3-4', [2, 1179]], ['2016-3-8', [5, 575]], ['2016-3-9', [1, 17]], ['2016-3-10', [1, 277]], ['2016-3-11', [2, 139]], ['2016-3-14', [1, 820]], ['2016-3-15', [2, 1148]], ['2016-3-16', [50, 11004]]], 'username': 'awilbur'}
    """
    method = 'GET'
    url = '/rest/v1/users/%s/usage' % user
    json_data = request(method, url)
    historical_usage = json.loads(json_data)
    return historical_usage

##############################################################
# Special Methods
# ---------------
# These do more complex things. Example - investigate() shows
# how many of a user's recent tests had errors
#
# Feel free to add your own, PRs welcome!
##############################################################

def investigate(user=DEFAULT_USER):
    """
        Show info about `user`'s errors (including the error and platform) for the last 100 jobs.
        This is intended to reveal trends about a user's recent tests.

        ex: supersauce.investigate('awilbur')

        >>> Platforms with errors:

            2   Windows 2008 iexplore 11
            2   Windows 10 iexplore 11
            8   Mac 10.11 safari 9

            Errors: 12 (out of 100)

            1   User terminated
            2   Test did not see a new command for 90 seconds. Timing out.
            2   Unsupported OS/browser/version/device combo: OS: 'Windows 10', Browser: 'iexplore', Version: '11.0.', Device: 'unspecified'
            3   Test exceeded maximum duration after 1800 seconds
            4   New session request was cancelled before a Sauce Labs virtual machine was found For help, please check https://docs.saucelabs.com/reference/troubleshooting-common-error-messages
    """
    jobs = getjobs(user) # loads 100 jobs. todo: load more?
    # if we do end up wanting more jobs, unfortunately I don't think there's
    # an endpoint that returns full job info for multiple jobs at once. (The
    # one we're using grabs 100, and I couldn't find a way to increase it or
    # skip jobs. The endpoints that do allow it only return job ids, so we
    # will probably need to pull full job info for each job id.)
    error_count = {}
    pass_count = {}
    error_msg = {}
    platform_key = ''

    for job in jobs:
        if job['error']:
            msg = job['error'].replace('\n', ' ')
            platform_key = '%s %s %s' % (job['os'], job['browser'], job['browser_short_version'])
            if error_count.get(platform_key) is None:
                error_count[platform_key] = 1
            else:
                error_count[platform_key] = error_count[platform_key] + 1
            if error_msg.get(msg) is None:
                error_msg[msg] = 1
            else:
                error_msg[msg] = error_msg[msg] + 1
        else:
            if pass_count.get(platform_key) is None:
                pass_count[platform_key] = 1
            else:
                pass_count[platform_key] = pass_count[platform_key] + 1
    total_errors = 0
    print 'Platforms with errors:\n'
    for k in sorted(error_count, key=error_count.get):
        print '%s\t%s' % (error_count[k], k)
        total_errors += error_count[k]
    print ''
    print "Errors: %s (out of %s)" % (str(total_errors), str(len(jobs)))
    print ''
    for k in sorted(error_msg, key=error_msg.get):
        print '%s\t%s' % (error_msg[k], k)

def update_latest_build(build, num_jobs=1):
    """
        Updates the latest `num_jobs` jobs belonging to SAUCE_USERNAME with the build name `build`.

        ex: supersauce.update_latest_build('Build X', 3)

        >>> (no output, but the latest 3 jobs are updated with 'Build X')
    """
    jobs = jobids(num_jobs)
    for id in jobs:
        update_job(id, build_num=build)