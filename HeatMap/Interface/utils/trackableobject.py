class TrackableObject:
	def __init__(self, objectID, centroid, counted, startTime, firstBody_id, alertNumber, alertStartTime, ch_id):
		# store the object ID, then initialize a list of centroids
		# using the current centroid
		self.objectID = objectID
		self.centroids = [centroid]
		self.counted = counted
		self.startTime = startTime
		self.firstBody_id = firstBody_id
		self.alertNumber = alertNumber
		self.alertStartTime = alertStartTime
		self.ch_id = ch_id
 
		# initialize a boolean used to indicate if the object has
		# already been counted or not
