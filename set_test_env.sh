#!/usr/bin/env bash
# set env variable for production

bash -c 'export SH_USER=sh_test_user; export SH_PWD=Sch_t3st_#3#_pwd; export SH_HOST=localhost; export SH_DATABASE=sh_test_db; export SH_ENV=test; exec bash'
# Note: its adviced to manualy copy the env variables and set them, because executing this script creates multiple 
# sub shells.
