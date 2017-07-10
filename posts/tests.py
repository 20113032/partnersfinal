# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import unittest
from posts.models import Client, Project, Message, Transaction
from django.contrib.auth.models import User
# Create your tests here.
class ModelsTestCase(unittest.TestCase):
    def setUpUser(self):
        User.objects.create(username="usernametest1", password="passwordtest1", email="emailtest1@gmail.com")
        User.objects.create(username="usernametest2", password="passwordtest2", email="emailtest2@gmail.com")
    def testUser(self):
        usernametest1=User.objects.get(username="usernametest1")
        usernametest2=User.objects.get(username="usernametest2")
        self.assertEqual(usernametest1.username, "usernametest1")
        self.assertEqual(usernametest2.username, "usernametest2")
        self.assertEqual(usernametest1.password, "passwordtest1")
        self.assertEqual(usernametest2.password, "passwordtest2")
        self.assertEqual(usernametest1.email, "emailtest1@gmail.com")
        self.assertEqual(usernametest2.email, "emailtest2@gmail.com")
    def setUpProject(self):
        Project.objects.create(user=usernametest1, projectname="projectnametest1", description="descriptiontest1", value=150)
        Project.objects.create(user=usernametest2, projectname="projectnametest2", description="descriptiontest2", value=160)
    def testProject(self):
        projecttest1=Project.objects.get(projectname="projectnametest1")
        projecttest2=Project.objects.get(projectname="projectnametest2")
        self.assertEqual(projecttest1.user, usernametest1)
        self.assertEqual(projecttest2.user, usernametest2)
        self.assertEqual(projecttest1.projectname, "projectnametest1")
        self.assertEqual(projecttest2.projectname, "projectnametest2")
        self.assertEqual(projecttest1.description, "descriptiontest1")
        self.assertEqual(projecttest2.description, "descriptiontest2")
        self.assertEqual(projecttest1.value, 150)
        self.assertEqual(projecttest2.value, 160)
    def setUpClient(self):
        Client.objects.create(user=usernametest1, firstname="firstnametest1", lastname="lastnametest1", usertype=1)
        Client.objects.create(user=usernametest2, firstname="firstnametest2", lastname="lastnametest2", usertype=2)
    def testClient(self):
        clienttest1=Client.objects.get(firstname="firstnametest1")
        clienttest2=Client.objects.get(firstname="firstnametest2")
        self.assertEqual(clienttest1.user, usernametest1)
        self.assertEqual(clienttest2.user, usernametest2)
        self.assertEqual(clienttest1.firstname, "firstnametest1")
        self.assertEqual(clienttest2.firstname, "firstnametest2")
        self.assertEqual(clienttest1.lastname, "lastnametest1")
        self.assertEqual(clienttest2.lastname, "lastnametest2")
        self.assertEqual(clienttest1.usertype, 1)
        self.assertEqual(clienttest2.usertype, 2)
    def setUpMessage(self):
        Message.objects.create(sender=usernametest1, recipient=usernametest2, project=projecttest1, title="titletest1", message="messagetest1")
        Message.objects.create(sender=usernametest2, recipient=usernametest1, project=projecttest2, title="titletest2", message="messagetest2")
    def testMessage(self):
        messagetest1=Message.objects.get(title="titletest1")
        messagetest2=Message.objects.get(title="titletest2")
        self.assertEqual(messagetest1.sender, usernametest1)
        self.assertEqual(messagetest2.sender, usernametest2)
        self.assertEqual(messagetest1.recipient, usernametest2)
        self.assertEqual(messagetest2.recipient, usernametest1)
        self.assertEqual(messagetest1.project, projecttest1)
        self.assertEqual(messagetest2.project, projecttest2)
        self.assertEqual(messagetest1.title, "titletest1")
        self.assertEqual(messagetest2.title, "titletest2")
        self.assertEqual(messagetest1.message, "messagetest1")
        self.assertEqual(messagetest2.message, "messagetest2")
    def setUpTransaction(self):
        Transaction.objects.create(backer=usernametest1, entreprenuer=usernametest2, project=projecttest1, ammount=50.0, valid="truth")
        Transaction.objects.create(backer=usernametest1, entreprenuer=usernametest2, project=projecttest2, ammount=40.0, valid="truth")
    def testTransaction(self):
        transactiontest1=Transaction.objects.get(ammount=50.0)
        transactiontest2=Transaction.objects.get(ammount=40.0)
        self.assertEqual(transactiontest1.backer, usernametest1)
        self.assertEqual(transactiontest2.backer, usernametest1)
        self.assertEqual(transactiontest1.entreprenuer, usernametest2)
        self.assertEqual(transactiontest2.entreprenuer, usernametest2)
        self.assertEqual(transactiontest1.project, projecttest1)
        self.assertEqual(transactiontest2.project, projecttest2)
        self.assertEqual(transactiontest1.ammount, 50.0)
        self.assertEqual(transactiontest2.ammount, 60.0)
        self.assertEqual(transactiontest1.valid, "truth")
        self.assertEqual(transactiontest2.valid, "truth")
    if __name__=="__main__":
        unittest.main()
