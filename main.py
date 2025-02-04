import hashlib
import random

def challenge():
  return random.randrange(0,100)
  


def hashing(secret):
  return hashlib.sha256(secret.encode()).hexdigest()


def proveKnowledge(secret):
  return hashing(secret);

def veifyKnowledge(hashedSecret, expectedSecret):
  flag = 0
  for i in range(0,100):
    hashExpectedSecret = hashing(expectedSecret+str(i))
    if(hashedSecret == hashExpectedSecret):
      flag = 1
      break
  if(flag == 1):
    return True
  else:
    return False


secret = "Treasure Loacation is ABC"
challengeValue  = challenge()
hashedSecret = proveKnowledge(secret+str(challengeValue))
expectedsecret = "Treasure Loacation is ABC"
if(veifyKnowledge(hashedSecret, expectedsecret)):
  print("Treasure locations are the same")
else:
  print("Treasure locations are NOT the same")
  
