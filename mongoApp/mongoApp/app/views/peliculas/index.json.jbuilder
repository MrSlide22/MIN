json.array!(@peliculas) do |pelicula|
  json.extract! pelicula, :id, :name, :description
  json.url pelicula_url(pelicula, format: :json)
end
