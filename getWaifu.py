import booru
import asyncio
import random

async def safe(tags):
    imgs = booru.safebooru()
    res = await imgs.search(query=tags, random=True, gacha=True)
    return(booru.resolve(res))

async def lewd(tags):
    imgs = booru.Danbooru()
    res = await imgs.search(query=tags, random=True, gacha=True)
    return(booru.resolve(res))

#print(asyncio.run(lewd("animated"))["file_url"])
#print(lewd("rem"))
