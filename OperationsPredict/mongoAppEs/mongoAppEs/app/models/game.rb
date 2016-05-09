class Game
  include Mongoid::Document
  field :name, type: String
  field :device, type: String
  field :likes, type: Integer


  def like
    self.likes ||= 0
    self.likes += 1 
    self.save!
  end
end
