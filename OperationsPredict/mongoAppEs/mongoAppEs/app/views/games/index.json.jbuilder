json.array!(@games) do |game|
  json.extract! game, :id, :name, :device
  json.url game_url(game, format: :json)
end
