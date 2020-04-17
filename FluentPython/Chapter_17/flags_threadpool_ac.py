from concurrent import futures

from flags import save_flag, get_flag, show, main # Reuse some functions from the flags module.


def download_one(cc): # Function to download a single image; this is what each thread will execute.
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def donwload_many(cc_list):
    cc_list = cc_list[:5] # For this demonstration, use only the top five most populous countries.
    with futures.ThreadPoolExecutor(MAX_WORKERS=3) as executor: # Hardcode max_workers to 3 so we can observe pending futures in the output.
        future = executor.submit(download_one, cc) # executor.submit schedules the callable to be executed, and returns a future representing this pending operation.
        to_do.append(future) # Store each future so we can later retrieve them with as_completed.
        msg = 'Scheduled for {}: {}'
        print(msg.format(cc, future)) # Display a message with the country code and the respective future.

    results = []
    for future in futures.as_completed(to_do): # as_completed yields futures as they are completed.
        res = future.result() # Get the result of this future. 
        msg = '{} result: {!r}'
        print(msg.format(future, res)) # Display the future and its result. 
        results.append(res)

    return len(results)