#!/usr/bin/env python3
import pymongo as mongodb
import Database
import datetime


mongoclient = mongodb.MongoClient("mongodb://localhost:27017/")
db = mongoclient.gdtechdb_prod

db.Sensors.insert_one(
	{
		"model":"gd",
            	"gateway_id":"gd",
            	"time": datetime.datetime.timestamp(datetime.datetime.now()),
	    	"gdtime":datetime.datetime.now()
	})


