import requests, json, concurrent.futures
import webcrawler

url = "https://graphql.anilist.co"

def queryMediaId(tuple: tuple) -> int:
    altUrl, title, token = tuple

    if "\"" in title: title = title.replace("\"", "\'")

    headers = {'Authorization': 'Bearer ' + token,
               'Content-Type': 'application/json',
               'Accept': 'application/json',
               'Connection': 'close'}
    query = 'query {{ Media(search:"{}", type:ANIME) {{ id title {{ english romaji native }} }} }}'.format(title)

    res = requests.post(url, headers=headers, json={'query': query})
    data = json.loads(res.text)
    print(data)
    queriedTitle = data["data"]["Media"]["title"]


    print("Requests remaining: " + str(res.headers["X-RateLimit-Remaining"]))
    if int(res.headers["X-RateLimit-Remaining"]) < 5:
        print("Sleep")
        time.sleep(1)


    queriedTitle = [qT.replace(" ", "").upper() if qT is not None else None for qT in queriedTitle.values()]

    print("after queried")

    if title.replace(" ", "").upper() in queriedTitle:
        return data["data"]["Media"]["id"]
    else:
        altNames = webcrawler.getAlternateNames(altUrl)
        print(title)
        print(altNames)
        print(queriedTitle)

        if not altNames: return 0
        for name in altNames:
            print(name)
            if name in queriedTitle: return data["data"]["Media"]["id"]
    return 0

def saveMediaListEntry(tupel: tuple) -> bool:
    id, status, episodesWatched, score, token = tupel

    headers = {'Authorization': 'Bearer ' + token,
               'Content-Type': 'application/json',
               'Accept': 'application/json',
               'Connection': 'close'}

    if status == "completed": status = webcrawler.Status.comp.value
    elif status == "currently-watching": status = webcrawler.Status.curr.value
    elif status == "dropped": status = webcrawler.Status.drop.value
    elif status == "on-hold": status = webcrawler.Status.hold.value
    elif status == "plan-to-watch": status = webcrawler.Status.plan.value

    query = "mutation {{ SaveMediaListEntry(mediaId:{}, status:{}, progress:{} {}) {{ mediaId }} }}".format(id, status, episodesWatched, " score:" + str(score) if score != None else "")
    res = requests.post(url, headers=headers, json={'query': query})

    print(res.status_code)

    return True if res.status_code == 200 else False

def addEntry(tupel: tuple) -> str:
    anime, status, token = tupel

    with concurrent.futures.ThreadPoolExecutor() as executor:
        medId = executor.submit(queryMediaId, (anime.url, anime.title, token))
        id = medId.result()
        if id != 0:
            medEntry = executor.submit(saveMediaListEntry, (id, status, anime.episodesWatched, anime.score, token))
            return medEntry.result()
            # return saveMediaListEntry(id, status, episodes, score)
        else:
            print("id 0")
            return False
