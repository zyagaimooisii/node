import scratchattach as scratch3

session = scratch3.login("splatoon-clips", "756851")
conn = session.connect_cloud("984167625")

conn.set_var("abc", 18)
