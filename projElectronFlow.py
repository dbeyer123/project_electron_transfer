'''
Project Electron Flow proj started on 7/10/17

TODO
	create parent class for bag item
	create methods for alerts out, checks on bag items

	wakeup cron batch to run methods its supposed to run

	
	Add in bagit
'''
## ingest number to have the system pull into the queue for processing
ingestItems = n

## import libraries

class bagitObj:
	## brain object

	__init__:
		## initialize client OBJ
		bagitClient = bagitClient()

		## requests active clients registry from API
		## every action in this object must be aware of this registry

		## determine based on the registry which folder to search ()

		## loop through files recently added
		## first validity check ---- check directories of inactive clients and see if something was pushed
			## this pushed content needs to be deleted and a notification sent out
			## eventLog(inactiveClient)
			## destroyPayload()

			## second ---- check active client directories for new files
				## perform basic validity checks on new files before they are added to queue
					## add in client id, size of file, name of file(s), timestamp of file creation, timestamp of queue creation
				
				## passes checks:
					## add in files to the queue based off of the timestamp from filedrop
					passBasicCheck()

				## fails check:
					##notification sent out
					## notifyClient(failValidityChecks)

		## application runs
			applicationRun()
	## method to fire when pass basic checks during addition to queue
	def passBasicCheck():
		## add the queue
		##add in client id, size of file, name of file(s), timestamp of file creation, timestamp of queue creation
		## wake up queue


	def failBasicCheck():

		## 

	## application run method with an argument that is used to control
	def applicationRun(ingestItems):
		## loop through ingestItems number if items in queue
			## start routine for the nth file
			## wakeup queue and ingests the new files' information
			## start virusCheck()
				##pass: move onto next check
					##success eventLog(virusCheckSuccess)
					## start validateCheck()
						## look into library for validity checks on Bagits
							## checks bagitPass() -- files exist, files placed correctly, and file structure is correct
						##pass: 
							##success eventLog(validateCheckSuccess)
							## notifyClient(Email)
							## pushFinalStorage(destination)
						##fail:
							bagitRoutineFailure(validateCheck) 

				##fail:

					bagitRoutineFailure(virusCheck)

	## method to be called on failure of file checks
	def bagitRoutineFailure(phase):
		##fail: add information from transaction to eventLog(failureMsg) - reason for fail, timestamp of fail, fileName, organizationID (source of File)
			##destroyPayload()
			##notifyClient(Email, failureMsg)

	## method for notifying customer
	def notifyClient():


class bagitClient:
	## bagit object used for client
	
	## set default values for client info
	clientID = 0
	clientName = "John Smith"
	activeStatus = 0
	clientEmail = "person@gmail.com"
	clientDir = "/client"

	## get client info from API

