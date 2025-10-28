from livereload import Server

server = Server()
server.watch("src/", delay=5)

server.serve(port=35729, host="127.0.0.1", root="*")