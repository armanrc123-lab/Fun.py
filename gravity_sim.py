from manim import *
import numpy as np

class Gravity(MovingCameraScene):
    def construct(self):
        earth = Circle(color=GREEN, radius=0.5, fill_color=BLUE, fill_opacity=1)
        moon = Circle(color=WHITE, radius=0.2, fill_color=WHITE, fill_opacity=1)
        mercury = Circle(color=GRAY, radius=0.3, fill_color=GRAY, fill_opacity=1)
        mars = Circle(color=RED, radius=0.4, fill_color=RED, fill_opacity=1)
        venus = Circle(color=GREEN, radius=0.5, fill_color=GREEN, fill_opacity=1)
        Jupiter = Circle(color=LIGHT_BROWN, radius=1.2, fill_color=LIGHT_BROWN, fill_opacity=1)
        sun =  Circle(color=YELLOW, radius=1.5, fill_color=ORANGE, fill_opacity=1)

        sun.move_to(ORIGIN)
        mercury.move_to(UP*12)
        venus.move_to(UP*22)
        earth.move_to(UP*30)
        moon.move_to(earth.get_center() + RIGHT*0.04)
        mars.move_to(UP*50)
        Jupiter.move_to(UP*70)


        saturn_height = 90


        planet = Circle(radius=1, color=GRAY_BROWN, fill_opacity=1).move_to(UP * saturn_height)
        planet.set_stroke(width=0.1)

        outer_ring = Annulus(inner_radius=1.1, outer_radius=1.3,
                             color=WHITE, fill_opacity=0.3)
        outer_ring.rotate(PI/6).move_to(UP * saturn_height)

        inner_ring = Annulus(inner_radius=1.3, outer_radius=1.5,
                             color=GRAY, fill_opacity=0.5)
        inner_ring.rotate(PI/6).move_to(UP * saturn_height)

        saturn = VGroup(planet, inner_ring, outer_ring)

        self.add(earth, moon, sun, saturn, Jupiter, mercury, venus, mars)

        self.camera.frame.scale(20)
        self.camera.frame.move_to(UP * 25)

        sun_mass     = 25000000
        mercury_mass = 5
        venus_mass   = 62.5
        earth_mass   = 75
        mars_mass    = 7.5
        jupiter_mass = 2500
        saturn_mass  = 750
        moon_mass    = 1


        def orbital_velocity(planet, central_body, central_mass):
            r_vec = planet.get_center() - central_body.get_center()
            r = np.linalg.norm(r_vec)
            if r == 0:
                return np.array([0.0, 0.0, 0.0])
            speed = np.sqrt(G * central_mass / r)
            direction = np.array([r_vec[1], -r_vec[0], 0]) / r
            velocity = np.array(speed * direction, dtype=float)

            return(velocity)


        G = 0.04
    

        bodies = []


        for mob, mass in [(earth, earth_mass), (sun, sun_mass), (saturn, saturn_mass), (mars, mars_mass),
            (mercury, mercury_mass), (venus, venus_mass), (Jupiter, jupiter_mass)]:

            velocity = orbital_velocity(mob, sun, sun_mass)
            bodies.append((mob, mass, velocity))

        v_earth = orbital_velocity(earth, sun, sun_mass)

        v_moon_rel = orbital_velocity(moon, earth, earth_mass)
        velocity_moon = v_earth + v_moon_rel
        bodies.append((moon, moon_mass, velocity_moon))
        bodies.append((sun, sun_mass, np.array([0.0, 0.0, 0.0])))


        def gravity_updater(body, bodies_list, dt):
            dt = 0.001
            pos = body.get_center()
            acceleration = np.zeros(3)

            for other_mob, other_mass, other_velocity in bodies_list:
                if other_mob is body:
                    continue
                r_vec = other_mob.get_center() - pos
                r = np.linalg.norm(r_vec)
                if r < 1e-6:
                    return
                acceleration += G * other_mass * r_vec / r**3

            for mob, _, velocity in bodies_list:
                if mob is body:
                    velocity += acceleration * dt
                    body.shift(velocity * dt)
                    break


        

        for mob, _, _ in bodies:
            mob.add_updater(lambda m, dt, mob=mob: gravity_updater(mob, bodies, dt))

    
        self.wait(240)
