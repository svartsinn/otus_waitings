#!/bin/bash

docker build -t tests .

docker run --name test_run tests pytest --browser $1

docker cp test_run:/app/allure-report .

allure serve allure-report

docker rm test_run