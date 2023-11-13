from vpython import sphere, vector, color, rate, canvas, text

scene = canvas(width=800, height=600)
xlen, ylen , zlen = 100, 100, 100
'''
boundaries = [
    box(pos = vector(0,-ylen/2,0), size = vector(xlen, .2, zlen)),
    box(pos = vector(0,ylen/2,0), size = vector(xlen, .2, zlen)),
    box(pos = vector(-xlen/2,0,0), size = vector(.2, ylen, zlen)),
    box(pos = vector(xlen/2,0,0), size = vector(.2, ylen, zlen)),
    box(pos = vector(0,0,-zlen/2), size = vector(xlen, ylen, .2))
    ]
'''
# 공 생성
ball = sphere(pos=vector(0, 0, 0), radius=5, color=color.red, make_trail=True)

velocity_text = text(pos=vector(-200, 7, 0), text='Velocity: ', height=10, align='left', color=color.white)
gravitational_acceleration_text = text(pos=vector(-200, 0, 0), text = 'Gravitational_Acceleration: 9.8 m/s²', height=5 , align='left', color=color.white)

# 초기 속도 설정
ball.velocity = vector(0, 1, 0)

# 뉴턴의 운동 방정식 시뮬레이션
while True:
    rate(120)  # 프레임 속도 설정 (120프레임/초)
    
    velocity_text.visible = False  # 이전 텍스트 숨기기
    velocity_text = text(pos=vector(-200, -15, 0), text='Velocity: {:.2f} m/s'.format(ball.velocity.mag), height=10, align='left', color=color.white)
    
    ball.pos = ball.pos + ball.velocity * 0.1  # 0.1초 동안의 이동
    ball.velocity.y = ball.velocity.y - 9.8 * 0.1  # 중력 적용
    
    bottom = (ylen / 2) - ball.radius
    
    if ball.pos.y < -150:
        break
    
