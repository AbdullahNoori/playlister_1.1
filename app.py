from pymongo import MongoClient

client = MongoClient()
db = client.Playlister
playlists = db.playlists

from flask import Flask, render_template,  request, redirect, url_for


app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # change the original return statement you wrote to the one below
    return render_template('home.html', msg='Flask is Cool!!')


# OUR MOCK ARRAY OF PROJECTS
# playlists = [
#     { 'title': 'Cat Videos', 'description': 'Cats acting weird' },
#     { 'title': '80\'s Music', 'description': 'Don\'t stop believing!' }
# ]

@app.route('/playlists')
def playlists_index():
    """Show all playlists."""
    return render_template('playlists_index.html', playlists=playlists)

@app.route('/playlists/new')
def playlists_new():
    """Create a new playlist."""
    return render_template('playlists_new.html')

@app.route('/playlists', methods=['POST'])
def playlists_submit():
    """Submit a new playlist."""
        playlist = {
        'title': request.form.get('title'),
        'description': request.form.get('description')
        'videos': videos,
        'video_ids': video_id

    playlists.insert_one(playlist
    return redirect(url_for('playlists_index'))

def video_url_creator(id_lst):
    videos = []
    for vid_id in id_lst:
        # We know that embedded YouTube videos always have this format
        video = 'https://youtube.com/embed/' + vid_id
        videos.append(video)
    return videos



if __name__ == '__main__':
    app.run(debug=True)


