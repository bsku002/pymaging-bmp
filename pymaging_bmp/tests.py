# -*- coding: utf-8 -*-PyPI now supports uploading project files for redistribution; uploaded files are easily found by EasyInstall, even if you don't have download links on your project's home page.


# Copyright (c) 2012, Jonas Obrist
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the Jonas Obrist nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL JONAS OBRIST BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
from pymaging_bmp.codec import BMPDecoder
from pymaging.utils import get_test_file
from pymaging.webcolors import Black, White, Red, Blue, Lime
import unittest


class BMPTests(unittest.TestCase):
    def test_32bit_bmp_decoding(self):
        with open(get_test_file(__file__, 'black-white-32bit.bmp'), 'rb') as fobj:
            decoder = BMPDecoder(fobj)
            img = decoder.get_image()
        self.assertEqual(img.width, 2)
        self.assertEqual(img.height, 2)
        self.assertEqual(img.palette, None)
        self.assertEqual(decoder.bits_per_pixel, 32)
        self.assertEqual(img.get_color(0, 0), Black)
        self.assertEqual(img.get_color(1, 1), Black)
        self.assertEqual(img.get_color(0, 1), White)
        self.assertEqual(img.get_color(1, 0), White)
        
    def test_32bit_bmp_decoding_colorful(self):
        with open(get_test_file(__file__, 'red-green-blue-black-32bit.bmp'), 'rb') as fobj:
            decoder = BMPDecoder(fobj)
            img = decoder.get_image()
        self.assertEqual(img.width, 2)
        self.assertEqual(img.height, 2)
        self.assertEqual(img.palette, None)
        self.assertEqual(decoder.bits_per_pixel, 32)
        self.assertEqual(img.get_color(0, 0), Red)
        self.assertEqual(img.get_color(1, 0), Lime)
        self.assertEqual(img.get_color(0, 1), Blue)
        self.assertEqual(img.get_color(1, 1), Black)
    
    def test_24bit_bmp_decoding(self):
        with open(get_test_file(__file__, 'black-white-24bit.bmp'), 'rb') as fobj:
            decoder = BMPDecoder(fobj)
            img = decoder.get_image()
        self.assertEqual(img.width, 2)
        self.assertEqual(img.height, 2)
        self.assertEqual(img.palette, None)
        self.assertEqual(decoder.bits_per_pixel, 24)
        self.assertEqual(img.get_color(0, 0), Black)
        self.assertEqual(img.get_color(1, 1), Black)
        self.assertEqual(img.get_color(0, 1), White)
        self.assertEqual(img.get_color(1, 0), White)
    
    def test_1bit_bmp_decoding(self):
        with open(get_test_file(__file__, 'black-white.bmp'), 'rb') as fobj:
            decoder = BMPDecoder(fobj)
            img = decoder.get_image()
        self.assertEqual(img.width, 2)
        self.assertEqual(img.height, 2)
        self.assertNotEqual(img.palette, None)
        self.assertEqual(decoder.bits_per_pixel, 1)
        self.assertEqual(img.get_color(0, 0), Black)
        self.assertEqual(img.get_color(1, 1), Black)
        self.assertEqual(img.get_color(0, 1), White)
        self.assertEqual(img.get_color(1, 0), White)
    
    def test_1bit_bmp_red_white_decoding(self):
        with open(get_test_file(__file__, 'red-white.bmp'), 'rb') as fobj:
            decoder = BMPDecoder(fobj)
            img = decoder.get_image()
        self.assertEqual(img.width, 2)
        self.assertEqual(img.height, 2)
        self.assertNotEqual(img.palette, None)
        self.assertEqual(decoder.bits_per_pixel, 1)
        self.assertEqual(img.get_color(0, 0), Red)
        self.assertEqual(img.get_color(1, 1), Red)
        self.assertEqual(img.get_color(0, 1), White)
        self.assertEqual(img.get_color(1, 0), White)
    
    def test_1bit_bmp_decoding_horizontal(self):
        with open(get_test_file(__file__, 'black-white-horizontal.bmp'), 'rb') as fobj:
            decoder = BMPDecoder(fobj)
            img = decoder.get_image()
        self.assertEqual(img.width, 2)
        self.assertEqual(img.height, 2)
        self.assertNotEqual(img.palette, None)
        self.assertEqual(decoder.bits_per_pixel, 1)
        self.assertEqual(img.get_color(0, 0), Black)
        self.assertEqual(img.get_color(1, 0), Black)
        self.assertEqual(img.get_color(0, 1), White)
        self.assertEqual(img.get_color(1, 1), White)
