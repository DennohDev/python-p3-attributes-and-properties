#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name = "name", job = None):
        if name == "" or (not(isinstance(name, str) and (1<= len(name) <= 25))):
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = name.title()
        if job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        else:
            self._job = job
    def get_name(self):
        print ("Getting name")
        return self._name
    def get_job(self):
        print("Getting Job")
        return self._job
    
    name = property(get_name)
    job = property(get_job)
