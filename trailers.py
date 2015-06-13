import os
import re
import webbrowser

'''trailers info'''

#table of templates and associated file locations
table_of_files = {
  'main_page_head': 'scripts/head.tpl',
  'main_page_content': 'scripts/index.tpl',
  'movie_tile_content': 'scripts/movie.tpl'
}

def create_movie_tiles_content(movies):
    '''The HTML content for this section of the page'''
    with open(table_of_files['movie_tile_content']) as fh:
      movie_tile_content = fh.read()
    fh.close()

    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            us_release_date=movie.us_release_date
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('trailers.html', 'w')

  with open(table_of_files['main_page_head']) as fh:
    main_page_head = fh.read()
  fh.close()

  with open(table_of_files['main_page_content']) as fh:
    main_page_content = fh.read()
  fh.close()

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible