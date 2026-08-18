tags = {"python", "data"}
 
tags.add("beginner")
tags.remove("data")
 
tags.discard("not_here")   # no error, even though it's missing === this method is safe for production apps
tags.remove("not_here")    # KeyError! unsafe for production apps