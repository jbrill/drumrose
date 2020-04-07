# DRUMROSE

:rocket: Welcome to the future of music :rocket:

## :memo: Where do I start?

### Step 1: Get a dev machine set up :bullettrain_side: 

- [ ] Get a droplet issued
- [ ] Generate ssh key for gitlab
- [ ] Pull the repository


---


### Step 2: Stand up the stack :fireworks:

You should be able to stand up the stack with `make up`. 

Our development environment runs on `docker-compose`, while our `staging` and `production` environments are served on their own `kubernetes` clusters.

:::info
:bulb: Some addition apt work may be required to get your development box in the proper state. 
:::


---


### Step 3: Start building :panda_face: 

1. To merge code, create a new branch off master with your initials as the prefix (i.e. `jb/authentication-microservice`)

2. After committing some code, specify either a `(feature)` or `(bug)` in the beginning of the commit message (i.e. `(feature) tornado service`)

3. Create a `merge request`
    - Make sure to check `Delete source branch when merge request is accepted.`
