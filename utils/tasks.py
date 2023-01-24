from datetime import datetime
from time import perf_counter

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from bot import bot
from service.users import get_users
from db.base import session

def create_html(counter, during):
    html = f"""
        <html>
            <head>
                <title>Report</title>
            </head>
            <body>
                <h2>Bot: @DistributionPythonBot</h1>
                <h4>Number of sent messages: {counter}</h4>
                <h4>Completed in: {during} seconds</h4>
            </body>
        </html>
    """
    time = datetime.now().strftime("%Y%m%d-%H%M%S")
    with open(f'report_{time}.html', 'w') as f:
        f.write(html)


async def send_message():
    start = perf_counter()
    users = await get_users(session)
    if not users:
        return
    counter = 0
    for user in users:
        await bot.send_message(user.tg_user_id, "I'ts schedule message")
        counter += 1
        if counter == 1000:
            break
    end = perf_counter()
    during = round(end - start, 2)
    create_html(counter, during)
    

def scheduled_task():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_message, 'interval', minutes=1)
    scheduler.start()