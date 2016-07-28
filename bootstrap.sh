#!/bin/bash

oc cluster up
oc login -u system:admin
oc adm policy add-cluster-role-to-user cluster-admin developer
oc adm policy add-scc-to-user privileged developer
oc adm policy add-scc-to-user privileged system:serviceaccount:guestbook:default
oc login -u developer
