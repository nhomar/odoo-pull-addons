Odoo Updater from Configfile.
---

Simple, you have an addons-path setted into some place, then you simply run

## Install

```
$ sudo pip install odoo-pull-addons
```

```
$ odoo-pull-addons path/to/config/file.conf
```

Then it will return all repositories updated.

Take care of few things:

1. It will run git pull simple, then your repositories shoudl has a default
   origin remote.
