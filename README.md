Ansible Role Monit
=========

[![Build Status](https://travis-ci.com/cloudweeb/cloudweeb.monit.svg?branch=master)](https://travis-ci.com/cloudweeb/cloudweeb.monit)

Ansible rolt to install Monit service

Requirements
------------

None

Role Variables
--------------

| Variable                | Default                      |  Comment                                         |
|-------------------------|------------------------------|--------------------------------------------------|
| monit_check_interval    | 120                          | Monit's poll cycle length                        |
| monit_start_delay       | 240                          | Time delay before Monit starts checking services |
| monit_http_port         | 2812                         | Monit http default port                          |
| monit_http_listen_addr  | localhost                    | Monit http listen address                        |
| monit_http_allow_access | ["localhost"]                | Monit http allow access                          |
| monit_enable_alert      | false                        | enable Monit alert if true                       |
| monit_alert_rcpt        | ['admin@{{ ansible_fqdn }}'] | Monit alert recipients                           |
| monit_alert_sender      | "admin@{{ ansible_fqdn }}"   | Monit alert sender                               |
| monit_mailserver        | ["localhost"]                | Monit SMTP host                                  |
| monit_mailserver_port   | 25                           | Monit SMTP port                                  |
| monit_mailserver_user   |                              | Monit SMTP user                                  |
| monit_mailserver_pass   |                              | Monit SMTP pass                                  |
| monit_mail_subject      | monit alert --  $EVENT       | Monit alert subject                              |
| monit_mail_message:     | defaults/main.yml#L20        |Monit alert message                               |
| monit_service_checks    | defaults/main.yml#L13        | Services that must be checked by monit           |

Dependencies
------------

* geerlingguy.repo-epel

Example Playbook
----------------

    - hosts: servers
      vars:
        monit_start_delay: ""

      roles:
        - role: geerlingguy.repo-epel
          when: ansible_distribution == 'RedHat'
        - role: cloudweeb.monit

License
-------

BSD / MIT

Author Information
------------------

Agnesius Santo Naibaho
