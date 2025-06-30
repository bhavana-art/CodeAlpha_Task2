#### TODO: Add Django Default Admin/Auth models 

* account
* Likes
* Comment
* Post
* Image
* Video
* setting 

* Connection 
* Group
* Events
* Contacts <- not yet.


### Relations ships

* (one-to-many) account_post: account <-- post,post,post
* (one-to-many) account_media image|video: account <-- image,video,image,video
* (one-to-many) media_like_account: media image|video <-- account,like
* (one-to-one) account_setting: account <-> setting (maybe a json object???)


### Connection

I connection is a Many-to-Many relationship to any `connectable entities`.
A `connectable entity` could be:

* account 
* group
* event

Now, this means that we could potentially have connections between different entities types (or same) and each would have a _different meaning_.
These are the possible combinations (no a definitive list);

* (friend) account <-> account (friend)
* (member) account <-> group (members)
* (participant) account <-> event (participants)
* (party) group <-> event (parties)

#### Connection status



###### Possible solutions / Schemas

```txt
# https://stackoverflow.com/a/31351505/13903942
USER_RELATIONSHIP {
    user_first_id,
    user_second_id,
    type

    primary key(user_first_id, user_second_id)
}

```




##### Likes - Comments

* (one-to-many) post_like_account: post <-- account,like
* (one-to-many) post_comment_account: post <-- account,comment

* (many-to-many) connection_account_account: account <--> account
* (one-to-many)  connection_group_account: group <-- account,account,account
* (one-to-many)  connection: event <-- group,group,account,account

### Notes


* I think media (image and video) should be really just a sub-type of a post
* post is a 'base class' or an 'object' that can be visible/not visble to others and can be 'reactable'
  * Maybe the subtype or 'mixin' can be a 'ReactMixin' where someone or some entity can react (so give comment, like and so on.. )
