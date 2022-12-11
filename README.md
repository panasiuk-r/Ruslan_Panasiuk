# Ruslan_Panasiuk
Build with: selenium

Getting started:

Install pytest (in this case it was instaled by using requirments.txt plugin)

Install selenium webdriver

Run script: by IDE or using fallowing command: pytest -s -v

Usage:

Script was made for testing web scenario that include five steps:

Logging in
Going to workshift adding form
Adding new workshift with specific content (Workshift`s name: RandomName(in this case 'Sun'), From: 06:00 AM, To: 06:00 PM, Assigned Employee: Odis Adalwin)
Check if data is added
Deleting new workshift and making sure if data is deleted
