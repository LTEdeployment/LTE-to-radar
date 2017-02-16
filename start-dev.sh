#!/bin/sh
cd frontend
exec ./start-dev.sh &
cd ../backend/service
exec ./start-dev.sh &
#cd ..
#exec ./start-dev.sh
