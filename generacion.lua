-- === MOTOR DE GENERACIÓN INFINITA CON TRAMPAS ===
local TAMANIO_BLOQUE = 4
local ultimaPosicionZ = 0
local contadorBloques = 0 -- Cuenta cuántos bloques se van creando

-- Función segura para crear bloques
local function crearBloque(zCoord)
	contadorBloques = contadorBloques + 1

	local bloque = Instance.new("Part")
	bloque.Size = Vector3.new(TAMANIO_BLOQUE, 1, TAMANIO_BLOQUE)
	bloque.Position = Vector3.new(0, 4, zCoord)
	bloque.Anchored = true
	bloque.Parent = game.Workspace

	-- LÓGICA MATEMÁTICA: Si ya pasamos los 20 bloques, hay probabilidad de trampas
	if contadorBloques > 20 and math.random(1, 4) == 1 then
		-- Es un bloque trampa (Rojo)
		bloque.BrickColor = BrickColor.new("Bright red")
		bloque.Material = Enum.Material.Neon
		bloque.Name = "Trampa"

		-- CÓDIGO PARA QUE MATE: Si el personaje lo toca, se reduce su vida a 0
		bloque.Touched:Connect(function(objetoTocado)
			local personaje = objetoTocado.Parent
			local humano = personaje:FindFirstChildOfClass("Humanoid")
			if humano then
				humano.Health = 0 -- Muere instantáneamente
			end
		end)
	else
		-- Es un bloque normal (Azul)
		bloque.BrickColor = BrickColor.new("Bright blue")
		bloque.Material = Enum.Material.Neon
		bloque.Name = "Camino"
	end
end

-- 1. Generamos el camino inicial seguro de 20 bloques (sin trampas)
for i = 1, 20 do
	crearBloque(ultimaPosicionZ)
	ultimaPosicionZ = ultimaPosicionZ + TAMANIO_BLOQUE
end

-- 2. Bucle principal que detecta tu movimiento
task.spawn(function()
	while true do
		task.wait(0.1)

		local personaje = game.Workspace:FindFirstChild("lexjuan") or game.Workspace:FindFirstChildOfClass("Model")
		if personaje and personaje:FindFirstChild("HumanoidRootPart") then
			local root = personaje.HumanoidRootPart

			-- Si te acercas al final del camino, genera más bloques adelante
			if root.Position.Z > (ultimaPosicionZ - 30) then
				crearBloque(ultimaPosicionZ)
				ultimaPosicionZ = ultimaPosicionZ + TAMANIO_BLOQUE
			end
		end
	end
end)
