from multiprocessing import Pool
import time
import requests

def getRandomDogPicture(url):
    image = requests.get(url)

    return image


if __name__ == '__main__':
    count = 30
    urls = []
    dog_url = 'https://dog.ceo/api/breeds/image/random'
    for i in range(1,count):
        urls.append(dog_url)
    with Pool(None) as p:
        start = time.time()
        results = p.imap(getRandomDogPicture, urls)
        print(results)
        for result in results:
            print(result.text)
        end = time.time()
        print(end - start)

    start = time.time()
    for val in range(1, count):
        print(getRandomDogPicture(dog_url).text)
    end = time.time()
    print(end - start)
