import asyncio
import random
import time

# By 斜飞  this is Cotasks Funcitons
class Co_tasks:
    def __init__(self):
        # Create a queue that we will use to store our "workload".
        self.queue = asyncio.Queue()
        self.tasks = [] 

    def Co_set_Count(self,index):#set any Numble tasks
        for item in range(index):
            self.queue.put_nowait(item)
        
    def Co_set_args(self,*args):#set arguments
        self.queue.put_nowait(*args)
            
    async def Co_Add_Task(self,func,*args):
        # Create three worker tasks to process the queue concurrently.
        
        self.tasks.append(asyncio.create_task(self.worker(self.queue,func)))

    async def Co_run(self):
        await self.queue.join()# Wait until the queue is fully processed.

    async def Co_cancel_Tasks(self):  # Wait until all worker tasks are cancelled.
        for task in self.tasks:
            task.cancel()
        await asyncio.gather(*self.tasks, return_exceptions=True)


    async def worker(self,queue,func):
        while queue.empty() == False:

            # Get a "work item" out of the queue.
            sleep_for = await queue.get()
            
            await func(*sleep_for)
            # Sleep for the "sleep_for" seconds.
            
            # Notify the queue that the "work item" has been processed.
            queue.task_done()
            #print(f"{name} has slept for {sleep_for:.2f} seconds")

async def thisfunc(*args):
    print(args[1])
    await asyncio.sleep(1)
import aiohttp



async def dy_get_Data(*args):
    print(args[1])
    redis=args[0]
    url = "https://baidu.com"
    payload={}
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'passport_csrf_token_default=af4196414688cef39cb51daa5974daed; passport_csrf_token=af4196414688cef39cb51daa5974daed; MONITOR_DEVICE_ID=49f3e9e4-cb08-49aa-9c63-59806bd0021f; toutiao_sso_user=cee3e4ffb0ae9db9a28948b699596935; toutiao_sso_user_ss=cee3e4ffb0ae9db9a28948b699596935; n_mh=3kfRSlcBDmkSuYX-kQIHruAtTu6mRPhjDgAbza1GsM4; sso_uid_tt=6d6d958d742a731e201e1ab92d81bbd4; sso_uid_tt_ss=6d6d958d742a731e201e1ab92d81bbd4; _tea_utm_cache_2631=undefined; business-account-center-csrf-secret=6b7e3a3e5571c4e4953f80b7a24a7885; business-account-center-csrf-token=gM4YqWQc-NbrldbLXxs3TqWVjomTkENlYmFc; _tea_utm_cache_1574=undefined; x-jupiter-uuid=1640929444556760; s_v_web_id=verify_kxtz0yb1_5t1S2RuV_wbIg_45wM_ANJh_IVW6DUNnG7eG; buyin_shop_type=23; ttwid=1%7CXbv2SzpizyZFcZL8zL8siMb_Hfk4_6EUiBP4eU5blrY%7C1640929465%7C030e4598cdf6358f1752fcdfd3a705b01f3a67aaef65600f8201ed78ce5aee97; sid_ucp_sso_v1=1.0.0-KDJkZWFhZTczNmFlODUxMGVhMGVjMjMwN2Y5ODA5NzIyODVmMDMxZTcKHgjY14CZpvXfBxC6sbqOBhimDCAMMIvnmP0FOAhAJhoCbGYiIGNlZTNlNGZmYjBhZTlkYjlhMjg5NDhiNjk5NTk2OTM1; ssid_ucp_sso_v1=1.0.0-KDJkZWFhZTczNmFlODUxMGVhMGVjMjMwN2Y5ODA5NzIyODVmMDMxZTcKHgjY14CZpvXfBxC6sbqOBhimDCAMMIvnmP0FOAhAJhoCbGYiIGNlZTNlNGZmYjBhZTlkYjlhMjg5NDhiNjk5NTk2OTM1; odin_tt=d3bf3cc31647555ad29cc08296f7041bd47dca42c6b7fe849c51115ae8e57cd24b16297941c14eefd06e346cdea5d6f04cec9748dae4e755d50a30b8d9877d0a; passport_auth_status_ss=19e09f14a3e7a6b75a312343bc4fb014%2C6ea3a1062ac8263a0b0870406a5fbb43; passport_auth_status=19e09f14a3e7a6b75a312343bc4fb014%2C6ea3a1062ac8263a0b0870406a5fbb43; buyin_app_id=1128; ucas_c0_ss_buyin=CkEKBTEuMC4wEKeIkZ6pk6bnYRi9LyCcnsCtqo3MByiPETDY14CZpvXfB0C8sbqOBki85faQBlCPvMOWw6fQ1WBYfBIUQz3QIQ7vkXD85fGbU1r3QNfRMmg; sid_guard=29dde5e9a326216ddf7ad1b6611d0bf0%7C1640929468%7C5184000%7CTue%2C+01-Mar-2022+05%3A44%3A28+GMT; uid_tt=05db4484cc16cfbf961eea309f553232; uid_tt_ss=05db4484cc16cfbf961eea309f553232; sid_tt=29dde5e9a326216ddf7ad1b6611d0bf0; sessionid=29dde5e9a326216ddf7ad1b6611d0bf0; sessionid_ss=29dde5e9a326216ddf7ad1b6611d0bf0; sid_ucp_v1=1.0.0-KDM2NDU1OGEwYWEzMDE0ZGRjYjRlZGMyZTgxNDQ3ZGViNWE0YjgyOWEKFgjY14CZpvXfBxC8sbqOBhiPETgIQCYaAmhsIiAyOWRkZTVlOWEzMjYyMTZkZGY3YWQxYjY2MTFkMGJmMA; ssid_ucp_v1=1.0.0-KDM2NDU1OGEwYWEzMDE0ZGRjYjRlZGMyZTgxNDQ3ZGViNWE0YjgyOWEKFgjY14CZpvXfBxC8sbqOBhiPETgIQCYaAmhsIiAyOWRkZTVlOWEzMjYyMTZkZGY3YWQxYjY2MTFkMGJmMA; ucas_c0_buyin=CkEKBTEuMC4wEKeIkZ6pk6bnYRi9LyCcnsCtqo3MByiPETDY14CZpvXfB0C8sbqOBki85faQBlCPvMOWw6fQ1WBYfBIUQz3QIQ7vkXD85fGbU1r3QNfRMmg; SASID=SID2_3523869204145161382; BUYIN_SASID=SID2_3523869204145161382; gftoken=MjlkZGU1ZTlhM3wxNjQwOTI5NDgwMTR8fDAGBgYGBgY; MONITOR_WEB_ID=4c430534-60fb-490d-b089-6053fa1ab124; tt_scid=0kJfOlSKP6eQCzwUdlsmvqveEP1DnjhcvGULsjThtqqHiWN7WSgjw6Mn2hm05tDkfc72; msToken=i4OJS3piO0gPumJaI4QDrzbThwX5K3SfbCH7seH9l11Y4Ik2c0DHUn22Niiuk9IbZGzmrQKxoHlSFKQhaUUuE6CzbYFW_EaAC07UbKi6ee316g8=; msToken=UedGcJSlOcSgzjZSrchf-dxGKEJEcDrpb3zVddl4m84LHOUOprgtmhalKHWT5dMV8uXcyb4ZPRiCh49YTwCAaBiWbkI4y-9XBH06c1898AdskxDv',
    'referer': 'https://buyin.jinritemai.com/dashboard/institution/serviceCharge',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as resp:
            data = await resp.text()

        return 
async def test():

    Co_task=Co_tasks()
    for item in range(100):
        args=(1,item,"3")
        Co_task.Co_set_args(args)
    for item in range(15):
        await Co_task.Co_Add_Task(dy_get_Data)
    
    await Co_task.Co_run()
    await Co_task.Co_cancel_Tasks()
    

if __name__ =="__main__":
    start_time = time.time()
    loop=asyncio.get_event_loop()
    loop.run_until_complete(test())
    print("执行完成")
    start_time = time.time() - start_time
    print(start_time)