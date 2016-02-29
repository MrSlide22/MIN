class PeliculasController < ApplicationController
  before_action :set_pelicula, only: [:show, :edit, :update, :destroy]

  # GET /peliculas
  # GET /peliculas.json
  def index
    @peliculas = Pelicula.all
  end

  def favoritos

  end

  # GET /peliculas/1
  # GET /peliculas/1.json
  def show
  end

  # GET /peliculas/new
  def new
    @pelicula = Pelicula.new
  end

  # GET /peliculas/1/edit
  def edit
  end

  # POST /peliculas
  # POST /peliculas.json
  def create
    @pelicula = Pelicula.new(pelicula_params)

    respond_to do |format|
      if @pelicula.save
        format.html { redirect_to @pelicula, notice: 'Pelicula was successfully created.' }
        format.json { render :show, status: :created, location: @pelicula }
      else
        format.html { render :new }
        format.json { render json: @pelicula.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /peliculas/1
  # PATCH/PUT /peliculas/1.json
  def update
    respond_to do |format|
      if @pelicula.update(pelicula_params)
        format.html { redirect_to @pelicula, notice: 'Pelicula was successfully updated.' }
        format.json { render :show, status: :ok, location: @pelicula }
      else
        format.html { render :edit }
        format.json { render json: @pelicula.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /peliculas/1
  # DELETE /peliculas/1.json
  def destroy
    @pelicula.destroy
    respond_to do |format|
      format.html { redirect_to peliculas_url, notice: 'Pelicula was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_pelicula
      @pelicula = Pelicula.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def pelicula_params
      params.require(:pelicula).permit(:name, :description)
    end
end
