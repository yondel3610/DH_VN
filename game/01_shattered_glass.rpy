## Shattered Glass for Ren'Py by Maurimo 
## Version 1.0

# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


# TRANSFORMS
# CRACKED GLASS TRANSFORM:
    # u_refraction : vec2 = The amount of offset applied to the refracted parts of the glass.
    # u_refraction_mouse_influence : vec2 = The amount of offset that the mouse position will apply on the refracted glass.
    # u_alpha_s : float = The alpha of the effect. Keep it at 1.0, it is useful for the transition only.
transform shattered_glass_transform:
    mesh True
    gl_drawable_resolution True
    shader 'shattered_glass.shader'
    u_glass_pattern "shattered_glass_over"
    u_glass_bg "shattered_glass_bg"
    u_refraction (25, 25)
    u_refraction_mouse_influence (6.0 ,6.0)
    function set_glass_mouse_pos

# BIG SHAKE TRANSFORM 
# mult = The shake will be multiplied by this. Higher values make it more intense, 0 will make it nothing.
# rate = The amount of time between shakes. A lower value will make it shake with more frequency.
# time = The amount of time until the shake ends.
transform bigshake(mult=1.0, rate=0.060, time = 0.5):
    block:
        linear rate xoffset (mult * +1.8) yoffset (mult * -5)
        linear rate xoffset (mult * -2.6) yoffset (mult * -1.7)
        linear rate xoffset (mult * +2.6) yoffset (mult * -1.7)
        linear rate xoffset (mult * -1.7) yoffset (mult * -4)
        linear rate xoffset (mult * +0)   yoffset (mult * +1)
        repeat
    time time
    xoffset 0 yoffset 0 

# TRANSITION:
    # duration = The amount of time that the transition will take. 
    # I recommend adjusting the easeout values, make it last longer, disappear in a different way, etc!
transform shattered_glass_transition(duration = 1, *, new_widget=None, old_widget=None):
    delay duration

    contains:
        new_widget
        events True
        alpha 1.0

    contains:
        old_widget
        events False
        pause (duration / 2)
        easeout (duration / 2) alpha 0.0
    
    contains:
        new_widget
        events False
        mesh True
        gl_drawable_resolution True
        shader 'shattered_glass_alpha.shader'
        u_glass_pattern "shattered_glass_over"
        u_glass_bg "shattered_glass_bg"
        u_refraction (25, 25)
        u_refraction_mouse_influence (6.0 ,6.0)
        parallel:
            function set_glass_mouse_pos
        parallel:
            pause (duration / 2)
            easeout (duration / 2) alpha 0.0

init python:
    def inv_lerp(a, b, v) -> float:
        """Inverse Linear Interpolation, get the fraction between a and b on which v resides.
        Examples
        --------
            0.5 == inv_lerp(0, 100, 50)
            0.8 == inv_lerp(1, 5, 4.2)
        """
        return (v - a) / (b - a)
    
    def set_glass_mouse_pos(trans, st, at):
        x, y = renpy.display.draw.get_mouse_pos()
        trans.u_reflection_x = inv_lerp(0, config.screen_width, (x - config.screen_width / 2))
        trans.u_reflection_y = inv_lerp(0, config.screen_height, (y - config.screen_height / 2))
        return 0
#SHADER DECLARATIONS
init -2 python:
    renpy.register_shader("shattered_glass.shader", variables="""
        varying vec2 v_tex_coord;
        varying vec2 v_position;

        uniform float u_lod_bias;
        uniform vec2 u_model_size;
        uniform sampler2D tex0;
        uniform sampler2D u_glass_pattern;
        uniform sampler2D u_glass_bg;
        uniform float u_reflection_x;
        uniform float u_reflection_y;
        
        uniform vec2 u_refraction;
        uniform vec2 u_refraction_mouse_influence;
        attribute vec4 a_position;
        attribute vec2 a_tex_coord;

    """, fragment_functions="""
        float blendOverlay(float base, float blend) {
            return base<0.5?(2.0*base*blend):(1.0-2.0*(1.0-base)*(1.0-blend));
        }

        vec3 blendOverlay(vec3 base, vec3 blend) {
            return vec3(blendOverlay(base.r,blend.r),blendOverlay(base.g,blend.g),blendOverlay(base.b,blend.b));
        }
    """,vertex_300="""
        v_tex_coord = a_tex_coord;
        v_position = a_position.xy;

    """, fragment_350="""
        vec2 pixel_size = (vec2(1.) / u_model_size);
        vec2 pixel_small_size = (vec2(3.0) / u_model_size);
        vec2 reflectionOffset = vec2(u_reflection_x, u_reflection_y);
        vec4 reflectionColor = vec4(1.0, 1.0, 1.0, 0.3);
        vec2 influence = u_refraction_mouse_influence * reflectionOffset;
        vec4 white = vec4(1.0);
        vec2 uv = v_tex_coord;

        vec4 broken_glass = texture2D(u_glass_pattern, uv);
        vec4 broken_glass_bg = texture2D(u_glass_bg, uv);
        vec3 stepped = smoothstep(0.0, 1.0, broken_glass.rgb);
        vec4 adjacentColor = texture2D(u_glass_pattern, uv + (pixel_small_size * reflectionOffset));

        if (broken_glass != white) {
            vec4 base = texture2D(tex0, uv);
            vec4 overlaid = vec4(blendOverlay(base.rgb, broken_glass_bg.rgb), broken_glass_bg.a);

            gl_FragColor = vec4(mix(base.rgb, overlaid.rgb, overlaid.a), base.a);
        }
        else if (adjacentColor.rgb != white.rgb) {
            gl_FragColor = vec4(mix(texture2D(tex0, uv).rgb * 1.5, white.rgb, adjacentColor.a * .2), 1.0);
        }
        else {
            vec4 glassCol = texture2D(tex0, uv + broken_glass.a * (pixel_size * (u_refraction + influence)));
            glassCol = vec4(glassCol.rgb * vec3(1.0), 1.0);
            gl_FragColor = glassCol;
        }
    """)

    renpy.register_shader("shattered_glass_alpha.shader", variables="""
        varying vec2 v_tex_coord;
        varying vec2 v_position;

        uniform float u_lod_bias;
        uniform vec2 u_model_size;
        uniform sampler2D tex0;
        uniform sampler2D u_glass_pattern;
        uniform sampler2D u_glass_bg;
        uniform float u_reflection_x;
        uniform float u_reflection_y;
        uniform vec2 u_refraction;
        uniform vec2 u_refraction_mouse_influence;
        attribute vec4 a_position;
        attribute vec2 a_tex_coord;

    """, fragment_functions="""
        float blendOverlay(float base, float blend) {
            return base<0.5?(2.0*base*blend):(1.0-2.0*(1.0-base)*(1.0-blend));
        }

        vec3 blendOverlay(vec3 base, vec3 blend) {
            return vec3(blendOverlay(base.r,blend.r),blendOverlay(base.g,blend.g),blendOverlay(base.b,blend.b));
        }
    """,vertex_300="""
        v_tex_coord = a_tex_coord;
        v_position = a_position.xy;

    """, fragment_350="""
        vec2 pixel_size = (vec2(1.) / u_model_size);
        vec2 pixel_small_size = (vec2(3.0) / u_model_size);
        vec2 reflectionOffset = vec2(u_reflection_x, u_reflection_y);
        vec4 reflectionColor = vec4(1.0, 1.0, 1.0, 0.3);
        vec2 influence = u_refraction_mouse_influence * reflectionOffset;
        vec4 white = vec4(1.0);
        vec2 uv = v_tex_coord;

        vec4 broken_glass = texture2D(u_glass_pattern, uv);
        vec4 broken_glass_bg = texture2D(u_glass_bg, uv);
        vec3 stepped = smoothstep(0.0, 1.0, broken_glass.rgb);
        vec4 adjacentColor = texture2D(u_glass_pattern, uv + (pixel_small_size * reflectionOffset));

        if (broken_glass != white) {
            gl_FragColor = broken_glass_bg;
        }
        else if (adjacentColor.rgb != white.rgb) {
            gl_FragColor = vec4(mix(texture2D(tex0, uv).rgb * 1.5, white.rgb, adjacentColor.a * .2), 1.0);
        }
        else {
            vec4 glassCol = texture2D(tex0, uv + broken_glass.a * (pixel_size * (u_refraction + influence)));
            gl_FragColor = glassCol;
        }
    """)