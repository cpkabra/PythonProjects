import threading, requests, bs4, os, time, glob

begin = time.time()
def clear_dir(directory):
    folder_path = directory + "/*"
    files = glob.glob(folder_path)
    for file in files:
        os.remove(file)
threads = []
os.makedirs("Comics", exist_ok=True)
comic_url = "https://xkcd.com/"
def download_comics(start, ending):
    for urlnum in range(start, ending + 1):
        response_page = requests.get(comic_url+str(urlnum))
        response_page.raise_for_status()
        img_element = bs4.BeautifulSoup(response_page.text, "html.parser").select("#comic img")
        if not img_element:
            print("Nothing found! ")
        else:
            images = requests.get(comic_url + img_element[0].get("src"))
            print("Downloading " + str(comic_url + img_element[0].get("src")))
            images.raise_for_status()
            writing_dir = open("Comics/" + str(time.time()), "wb")
            for chunk in images.iter_content(100000):
                writing_dir.write(chunk)
def threaded_download(start, ending):
    for i in range(start, ending, 2):
        thread = threading.Thread(target=download_comics,args=(i, i+1))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print()
    print("Done downloading!")

clear_dir("Comics")
start_comic = int(input("Please enter starting comic( >= 1): "))
ending_comic = int(input("please enter ending comic ( <= 2297): "))
print()
threaded_download(start_comic,ending_comic)
print("Downloaded " + str((ending_comic - start_comic) + 1) + " comics in : " + str(round(time.time()-begin, 2)) + " seconds.")






