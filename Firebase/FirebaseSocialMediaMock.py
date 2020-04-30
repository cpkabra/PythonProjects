import Firebase.BackendAndValidation as bv

neel = bv.get_hashed_user("Neel Patel", "neelpatel104@gmail.com")
vedant = bv.get_hashed_user("Vedant Dulori", "vsdulori@gmail.com")
anisha = bv.get_hashed_user("Anisha Ponnapati", "aponnap@gmail.com")
jinkle = bv.get_hashed_user("Jinkle Mehta", "jmehta200@gmail.com")
users = [neel, vedant, anisha, jinkle]

bv.unfollow(anisha, vedant)
bv.unfollow(jinkle, vedant)
bv.unfollow(neel, vedant)