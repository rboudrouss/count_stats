# API

## URLS
- message/ : can do *anything* related to messages
    - `history/` : get all messages
    - `usermsg/` : get all user messages, need `id` variable
    - `datemsg/` : get all messages on a date or between 2 dates, need at least one of those : `maxd` or `mind`
    - `userdate/`: get all messages of a user between 2 dates, need `id` and `mard` or `mind`
    - `msginfo/` : get a specific information about the messages of the user between 2 dates, in addition of previous variabe, it needs `info`
- `user/` :  can do *anything*² related to users data
    - `users/` : get **all** user information
    - `user/`  : get informations about a specific user, require `id` variable