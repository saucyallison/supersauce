(Work in progress.)

I created this for maximum convenience for using the Sauce Labs REST API. Commands are designed to be short and memorable!


### Job info

List recent jobs id's belonging to the user (up to `limit`).

```
    supersauce.get_job_ids(3)
    supersauce.jobids(3)

>>> ['f74ea0fa26a24f0296866624dcc648fb', 'ecfa42b873e9466da1bc18da2b10f950', 'c23f7e304a2643eda5e5aea6189420e1']
```


Get full info for latest 100 jobs belonging to `user` (defaults to SAUCE_USERNAME).

```
    supersauce.get_jobs('awilbur')
    supersauce.getjobs('awilbur')
    supersauce.jobs('awilbur')

>>> [{'browser_short_version': '9', 'video_url': 'https://saucelabs.com/jobs/f74ea0fa26a24f0296866624dcc648fb/video.flv', 'creation_time': 1458104287, 'custom-data': None, 'browser_version': '9.0.', 'owner': 'awilbur', 'id': 'f74ea0fa26a24f0296866624dcc648fb', 'record_screenshots': True, 'record_video': True, 'build': None, 'passed': None, 'public': None, 'assigned_tunnel_id': None, 'status': 'complete', 'log_url': 'https://saucelabs.com/jobs/f74ea0fa26a24f0296866624dcc648fb/selenium-server.log', 'start_time': 1458104287, 'proxied': False, 'modification_time': 1458104378, 'tags': [], 'consolidated_status': 'complete', 'commands_not_successful': 1, 'name': None, 'end_time': 1458104378, 'error': None, 'os': 'Mac 10.11', 'breakpointed': None, 'browser': 'safari'},
    ... (x99)
    ]
```


Get a single job's full info for `user`'s job with id `jobid`.

```
    supersauce.get_job('awilbur', 'f74ea0fa26a24f0296866624dcc648fb')
    supersauce.getjob('awilbur', 'f74ea0fa26a24f0296866624dcc648fb')

>>> {'browser_short_version': '9', 'video_url': 'https://saucelabs.com/jobs/f74ea0fa26a24f0296866624dcc648fb/video.flv', 'creation_time': 1458104287, 'custom-data': None, 'browser_version': '9.0.', 'owner': 'awilbur', 'automation_backend': 'webdriver', 'id': 'f74ea0fa26a24f0296866624dcc648fb', 'collects_automator_log': False, 'record_screenshots': True, 'record_video': True, 'build': None, 'passed': None, 'public': None, 'end_time': 1458104378, 'status': 'complete', 'log_url': 'https://saucelabs.com/jobs/f74ea0fa26a24f0296866624dcc648fb/selenium-server.log', 'start_time': 1458104287, 'proxied': False, 'modification_time': 1458104378, 'tags': [], 'consolidated_status': 'complete', 'commands_not_successful': 1, 'name': None, 'selenium_version': '2.48.0', 'manual': False, 'assigned_tunnel_id': None, 'error': None, 'os': 'Mac 10.11', 'breakpointed': None, 'browser': 'safari'}
```


List all of `user`'s jobs since the unix timestamp `fromtime`.

```
    supersauce.jobsfrom('awilbur', 1458101920)

>>> [{'id': 'f74ea0fa26a24f0296866624dcc648fb'}, {'id': 'ecfa42b873e9466da1bc18da2b10f950'}, {'id': 'c23f7e304a2643eda5e5aea6189420e1'}, {'id': 'c03e8bb16fc54fddb7c521ab72d49d38'}, {'id': 'bee47807422d4c8796f581017efc1fb5'}, {'id': 'be73bef773b144e08644c3453b171110'}]
```


List all of `user`'s jobs in the range of unix timestamps `fromtime` until `totime`.

```
    supersauce.jobsfromto('awilbur', 1458101620, 1458101920)

>>> [{'id': 'e40108a6081e419b83797f748d66eeba'}, {'id': 'e18ed89b49754074bdfd64af492bf062'}, {'id': 'bf75c08a93164ffa9e661a4839ead3ea'}, {'id': '90ddefddafa44f5ba1ac649a99321007'}, {'id': '8bbf842ab3654a7bb63bbc71c22240cc'}, {'id': '7e8886ab496b4d568f5fdd0fdd6e96a4'}, {'id': '75ac5bb424fe40c7a4b5ec2aef505690'}, {'id': '50cab4505b4c4ab08fc4b8631069789d'}, {'id': '2f3c6635767a4ad9824935ad579054c0'}, {'id': '2628e61ed13a411eae36db11be659afc'}]
```


Get full info `user`'s latest (single) job.

```
    supersauce.latest('awilbur')

>>> {'browser_short_version': '9', 'video_url': 'https://saucelabs.com/jobs/f74ea0fa26a24f0296866624dcc648fb/video.flv', 'creation_time': 1458104287, 'custom-data': None, 'browser_version': '9.0.', 'owner': 'awilbur', 'automation_backend': 'webdriver', 'id': 'f74ea0fa26a24f0296866624dcc648fb', 'collects_automator_log': False, 'record_screenshots': True, 'record_video': True, 'build': None, 'passed': None, 'public': None, 'end_time': 1458104378, 'status': 'complete', 'log_url': 'https://saucelabs.com/jobs/f74ea0fa26a24f0296866624dcc648fb/selenium-server.log', 'start_time': 1458104287, 'proxied': False, 'modification_time': 1458104378, 'tags': [], 'consolidated_status': 'complete', 'commands_not_successful': 1, 'name': None, 'selenium_version': '2.48.0', 'manual': False, 'assigned_tunnel_id': None, 'error': None, 'os': 'Mac 10.11', 'breakpointed': None, 'browser': 'safari'}
```


Update your job `jobid` (or 'latest'/'L'/'l') to `newname`.

```
    supersauce.updatename('f74ea0fa26a24f0296866624dcc648fb', 'much better name')

>>> {'browser_short_version': '9', 'video_url': 'https://saucelabs.com/jobs/f74ea0fa26a24f0296866624dcc648fb/video.flv', 'creation_time': 1458104287, 'custom-data': None, 'browser_version': '9.0.', 'owner': 'awilbur', 'id': 'f74ea0fa26a24f0296866624dcc648fb', 'record_screenshots': True, 'record_video': True, 'build': None, 'passed': None, 'public': None, 'end_time': 1458104378, 'status': 'complete', 'log_url': 'https://saucelabs.com/jobs/f74ea0fa26a24f0296866624dcc648fb/selenium-server.log', 'start_time': 1458104287, 'proxied': False, 'modification_time': 1458146404, 'tags': [], 'consolidated_status': 'complete', 'commands_not_successful': 1, 'name': 'much better name', 'assigned_tunnel_id': None, 'error': None, 'os': 'Mac 10.11', 'breakpointed': None, 'browser': 'safari'}
```


Update attributes for the specified job.


Options:
```
    name
    build_num
    passed
    public
    tags
    custom_data
```
```
    supersauce.update_job('f74ea0fa26a24f0296866624dcc648fb', build_num='newbuild', passed=True)

>>> {'browser_short_version': '9', 'video_url': 'https://saucelabs.com/jobs/f74ea0fa26a24f0296866624dcc648fb/video.flv', 'creation_time': 1458104287, 'custom-data': None, 'browser_version': '9.0.', 'owner': 'awilbur', 'id': 'f74ea0fa26a24f0296866624dcc648fb', 'record_screenshots': True, 'record_video': True, 'build': 'newbuild', 'passed': True, 'public': None, 'end_time': 1458104378, 'status': 'complete', 'log_url': 'https://saucelabs.com/jobs/f74ea0fa26a24f0296866624dcc648fb/selenium-server.log', 'start_time': 1458104287, 'proxied': False, 'modification_time': 1458150018, 'tags': [], 'consolidated_status': 'passed', 'commands_not_successful': 1, 'name': 'much better name', 'assigned_tunnel_id': None, 'error': None, 'os': 'Mac 10.11', 'breakpointed': None, 'browser': 'safari'}
```


List all of `user`'s jobs in the range of unix timestamps `fromtime` until `totime`.

```
    supersauce.jobsfromto('awilbur', 1458101620, 1458101920)

>>> [{'id': 'e40108a6081e419b83797f748d66eeba'}, {'id': 'e18ed89b49754074bdfd64af492bf062'}, {'id': 'bf75c08a93164ffa9e661a4839ead3ea'}, {'id': '90ddefddafa44f5ba1ac649a99321007'}, {'id': '8bbf842ab3654a7bb63bbc71c22240cc'}, {'id': '7e8886ab496b4d568f5fdd0fdd6e96a4'}, {'id': '75ac5bb424fe40c7a4b5ec2aef505690'}, {'id': '50cab4505b4c4ab08fc4b8631069789d'}, {'id': '2f3c6635767a4ad9824935ad579054c0'}, {'id': '2628e61ed13a411eae36db11be659afc'}]
```


List all active tunnels from `user`.

```
    supersauce.get_tunnels('awilbur')
    supersauce.gettuns('awilbur')
    supersauce.tunnels('awilbur')
    supersauce.tuns('awilbur')

>>> ['11f0171429904a2dbd84d36ad0e8c171']
```


Calls the activity endpoint for `user`, displaying real-time concurrency usage for all subaccounts.

```
    supersauce.activity('awilbur')

>>> {'subaccounts': {'awilbursub2': {'in progress': 0, 'all': 0, 'queued': 0}, 'awilbursub': {'in progress': 0, 'all': 0, 'queued': 0}, 'TrueBlue': {'in progress': 0, 'all': 0, 'queued': 0}, 'BigRed': {'in progress': 0, 'all': 0, 'queued': 0}, 'YOUR_USERNAME': {'in progress': 0, 'all': 0, 'queued': 0}, 'awilbur_sub': {'in progress': 0, 'all': 0, 'queued': 0}, 'demo-user': {'in progress': 0, 'all': 0, 'queued': 0}, 'awilbur': {'in progress': 0, 'all': 0, 'queued': 0}, 'TrueBlue2': {'in progress': 0, 'all': 0, 'queued': 0}}, 'totals': {'in progress': 0, 'all': 0, 'queued': 0}}
```


List the subaccounts belonging to `user`.

```
    supersauce.get_subs('awilbur')
    supersauce.getsubs('awilbur')
    supersauce.subaccounts('awilbur')
    supersauce.subs('awilbur')

>>> ['BigRed', 'demo-user', 'TrueBlue', 'awilbursub2', 'YOUR_USERNAME', 'awilbur_sub', 'awilbursub', 'TrueBlue2']
```


Returns account information for `user`.

```
    supersauce.get_account_details('awilbur')

>>> {'domain': None, 'last_name': None, 'creation_time': 1398107526, 'user_type': 'admin', 'concurrency_limit': {'mac': 100, 'scout': 100, 'overall': 100, 'real_device': 30}, 'manual_minutes': 'infinite', 'can_run_manual': True, 'prevent_emails': ['marketing'], 'id': 'awilbur', 'first_name': None, 'verified': True, 'subscribed': False, 'title': None, 'ancestor_allows_subaccounts': True, 'ancestor': 'awilbur', 'email': 'allison@saucelabs.com', 'username': 'awilbur', 'access_key': '4b7b6bcc-1a60-41a4-b98e-cce10ac12ada', 'parent': None, 'is_admin': None, 'is_public': False, 'vm_lockdown': False, 'name': 'Allison Wilbur', 'is_sso': False, 'entity_type': 'individual', 'ancestor_concurrency_limit': {'mac': 100, 'scout': 100, 'overall': 100, 'real_device': 30}, 'minutes': 'infinite'}
```


Access the current status of Sauce Labs' services.

```
    supersauce.get_status()

>>> {'wait_time': 3.6167102966841185, 'service_operational': True, 'status_message': 'Basic service status checks passed.'}
```


Get list of all browsers currently supported on Sauce Labs.

`type` defaults to 'webdriver'. ('appium' and 'all' are also supported.)

```
    supersauce.get_browsers()

>>> [{'short_version': '7.0', 'long_name': 'iPad', 'api_name': 'ipad', 'long_version': '7.0.', 'device': 'ipad', 'latest_stable_version': '', 'automation_backend': 'webdriver', 'os': 'Mac 10.9'}, {'short_version': '7.1', ...
    ...
    ]
```


Access historical account usage.

```
    supersauce.get_historical_usage()

>>> {'usage': [['2016-1-20', [2, 24]], ['2016-1-21', [5, 1185]], ['2016-1-22', [245, 44507]], ['2016-1-23', [100, 8197]], ['2016-1-25', [3, 482]], ['2016-1-26', [1, 14]], ['2016-1-27', [100, 8904]], ['2016-2-4', [6, 296]], ['2016-2-5', [2, 26]], ['2016-2-9', [1, 53]], ['2016-2-10', [1, 64]], ['2016-2-11', [4, 219]], ['2016-2-12', [24, 13910]], ['2016-2-13', [330, 31796]], ['2016-2-16', [2, 21]], ['2016-2-17', [404, 15329]], ['2016-2-18', [2, 4622]], ['2016-2-19', [4, 3337]], ['2016-2-24', [1, 33]], ['2016-2-25', [512, 144174]], ['2016-2-26', [3, 479]], ['2016-2-27', [1, 5622]], ['2016-3-1', [4, 911]], ['2016-3-3', [4, 1452]], ['2016-3-4', [2, 1179]], ['2016-3-8', [5, 575]], ['2016-3-9', [1, 17]], ['2016-3-10', [1, 277]], ['2016-3-11', [2, 139]], ['2016-3-14', [1, 820]], ['2016-3-15', [2, 1148]], ['2016-3-16', [50, 11004]]], 'username': 'awilbur'}
```


# Special Methods

These do more complex things. Example - investigate() shows how many of a user's recent tests had errors.

Feel free to add your own, PRs welcome!


```
        supersauce.investigate('awilbur')

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
```


Update the latest `num_jobs` jobs belonging to SAUCE_USERNAME with the build name `build`.

```
        supersauce.update_latest_build('Build X', 3)

        >>> (no output, but the latest 3 jobs are updated with 'Build X')
```