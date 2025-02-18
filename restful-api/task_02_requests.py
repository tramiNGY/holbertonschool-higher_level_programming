#!/usr/bin/python3
'''
This module contains 2 functions to fetch posts from JSONPlaceholder
'''
import requests
import csv


def fetch_and_print_posts():
    """fetches all posts and print status code and titles"""
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {r.status_code}")
    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """saves posts into csv file"""
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {r.status_code}")
    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post['title'])

    with open('posts.cvs', mode='w', encoding="utf-8") as f:
        keys = ["id", "title", "body"]
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for post in posts:
            writer.writerow({key: post[key] for key in keys})
