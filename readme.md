# Project Name

Stream Bio-Sensor Data to Google BigQuery using Pub/Sub

## Table of Contents

- [Project Name](#project-name)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Features](#features)
  - [Installation](#installation)
  - [Note](#note)

## Description

The purpose of this data pipeline is to demonstrate live streaming of bio sensor-related (e.g., Apple Watch, FitBit, etc) messages generated to a Google Cloud Platform (GCP) Pub/Sub topic and storing that data for downstream analytics in a Google BigQuery (GBQ) table.

## Features

  - Users can customize the randomly generated bio-sensor data using the sensor_publisher.py application. 
  - Transformed data ready for analytics is stored in Google BigQuery (GBQ) via subscription service.

## Installation

Set Up GCP Access:
First, pick a GCP project to work from. Set up a new service account for the Google Cloud project that has permissions to send data to a Pub/Sub topic. Edit the default Service Account generated when you enable the Pub/Sub service on GCP to have GBQ Data Editor permissions. This is needed to push the messages to the GBQ target.

Prep your application environment:
  1. Install requirements.txt
  2. Create and store your .env file in your root directory. It should contain the following:
        - GOOGLE_APPLICATION_CREDENTIALS='Your new service account credentials.json'
        - TOPIC_PATH="projects/[GCP PROJECT ID]/topics/[PUB SUB TOPIC]"

Set up GBQ:
  1. Execute gbq_schema.py to generate your json file containing your message schema. If you edit the message contents in sensor_publisher.py then you have to update gbq_schema.py accordingly. 
  2. In your GCP project, navigate to GBQ and create a target dataset and table. Keep all the default settings as-is and create the schema using the text option, inserting the contents of your schema.json generated by gbq_schema.py.

Set up the topic and subscription in Pub/Sub by:
  1. Create a topic to send your bio-sensor data to. This is the topic you'll store in your .env file. Note: For troubleshooting purposes, I recommend electing to include a default subscription and pulling it as needed.
  2. Create a new subscription to the topic. Configure the subscription's Delivery Type ('Write to BigQuery'), target GBQ dataset and table (what you created in the above GBQ section), Schema Configuration ('Use table schema'). Note: You can opt to set up a new dead letter topic. This is useful for investigating pipeline errors - particularly if you are making changes to the message schema.

Finally, get the data moving: 
  1. Once the above steps are taken care of, execute sensor_publisher.py and watch the data flow into your target GBQ table. 

## Note
If you want to do transformations of the data after it hits the Topic but pre-GBQ you can use a managed service like GCP Dataflow. Otherwise, GCP makes it easy to plug the data into GBQ (or GCS for the matter) using a subscription service as described above.
