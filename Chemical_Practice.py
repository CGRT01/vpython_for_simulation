from vpython import sphere, vector, color, compound

# 수소 원자
H1 = sphere(pos=vector(-0.5, 1, 0), radius=0.6, color=color.white)
H2 = sphere(pos=vector(0.5, 1, 0), radius=0.6, color=color.white)

# 산소 원자
O = sphere(pos=vector(0, 0, 0), radius=0.9, color=color.red)

# 물 분자 생성
water_molecule = compound([H1, H2, O], pos=vector(0, 0, 0))

# 수소 원자 이동
H1.pos = vector(-0.5, 1, 0)
H2.pos = vector(0.5, 1, 0)

# 물 분자 위치 업데이트
water_molecule.pos = (H1.pos + H2.pos + O.pos) / 3

