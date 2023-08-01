# Issue:

Having a foreign key across several schemas does not work well with alembic autogenerate.  
While the first migration will look as expected, all following will drop and recreate the constraint again.  
Expected: Following migrations do not touch the constraint (as it is not changed)

# Reproduction

requires docker, docker-compose and poetry to be installed, then run with `./run.sh`
