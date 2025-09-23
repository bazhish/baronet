import pygame
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from frontend.recursos.imagens.cenario.cenario_explorar import arbusto_0, arbusto_2, arbusto_1, arbusto_3, arvore_grande_0, arvore_grande_1, arvore_pequena_0, arvore_pequena_1, arvore_pequena_2, arvore_pequena_3, barril_0, barril_1, barril_2, cogumelo_0, pedras_0, pedras_1, pedras_2, pedras_3, LArgura, casa_pequena0

class arvore_pequena:
    def __init__(self, x, y, largura, altura, imagem_pach, pos_chao_x, pos_chao_y):
        self.x = x * LArgura // 1920
        self.y = y * LArgura // 1920
        self.pos_chao_x = pos_chao_x
        self.pos_chao_y = pos_chao_y
        self.largura =  largura * LArgura // 1920
        self.altura = altura * LArgura // 1920
        self.imagem_pach = imagem_pach
        self.bottom_left = 150
        self.bottom_rith = 33
    
    def rect(self):
        """Retorna um pygame.Rect para usar na colisão"""
        return pygame.Rect(32 * LArgura // 1920 + (((self.x - 500) * 19200) // (1380 - 500) + self.pos_chao_x),
                            156 * LArgura // 1920 + (((self.y - 100) * 19200) // (980 - 100) + self.pos_chao_y),
                              60 * LArgura // 1920, 20 * LArgura // 1920)
    
class arvore_grande:
    def __init__(self, x, y, largura, altura, imagem_pach, pos_chao_x, pos_chao_y):
        self.x = x * LArgura // 1920
        self.y = y * LArgura // 1920
        self.pos_chao_x = pos_chao_x
        self.pos_chao_y = pos_chao_y
        self.largura =  largura * LArgura // 1920
        self.altura = altura * LArgura // 1920
        self.imagem_pach = imagem_pach
        self.bottom_left = 300
        self.bottom_rith = 30
    
    def rect(self):
        """Retorna um pygame.Rect para usar na colisão"""
        return pygame.Rect(30 * LArgura // 1920 + (((self.x - 500) * 19200) // (1380 - 500) + self.pos_chao_x),
                            300 * LArgura // 1920 + (((self.y - 100) * 19200) // (980 - 100) + self.pos_chao_y),
                              200 * LArgura // 1920, 60 * LArgura // 1920)
    
class barril:
    def __init__(self, x, y, largura, altura, imagem_pach, pos_chao_x, pos_chao_y):
        self.x = x * LArgura // 1920
        self.y = y * LArgura // 1920
        self.pos_chao_x = pos_chao_x
        self.pos_chao_y = pos_chao_y
        self.largura =  largura * LArgura // 1920
        self.altura = altura * LArgura // 1920
        self.imagem_pach = imagem_pach
        self.bottom_left = 48
        self.bottom_rith = 0
    
    def rect(self):
        """Retorna um pygame.Rect para usar na colisão"""
        return pygame.Rect(0 + (((self.x - 500) * 19200) // (1380 - 500) + self.pos_chao_x),
                            45 * LArgura // 1920 + (((self.y - 100) * 19200) // (980 - 100) + self.pos_chao_y),
                            40 * LArgura // 1920, 15 * LArgura // 1920)

class casa_pequena:
    def __init__(self, x, y, largura, altura, imagem_pach, pos_chao_x, pos_chao_y):
        self.x = x * LArgura // 1920
        self.y = y * LArgura // 1920
        self.pos_chao_x = pos_chao_x
        self.pos_chao_y = pos_chao_y
        self.largura =  largura * LArgura // 1920
        self.altura = altura * LArgura // 1920
        self.imagem_pach = imagem_pach
        self.bottom_left = 170
        self.bottom_rith = 25
    
    def rect(self):
        """Retorna um pygame.Rect para usar na colisão"""
        return pygame.Rect(20 * LArgura // 1920 + (((self.x - 500) * 19200) // (1380 - 500) + self.pos_chao_x),
                            170 * LArgura // 1920 + (((self.y - 100) * 19200) // (980 - 100) + self.pos_chao_y),
                              243 * LArgura // 1920, 90 * LArgura // 1920)

coordenadas = [(534, 107, "arvore_grande"), (632, 101, "arvore_grande"), (804, 99, "arvore_grande"), (804, 101, "arvore_grande"), (940, 104, "arvore_grande"), (1042, 101, "arvore_grande"),
               (1080, 102, "arvore_grande"), (1124, 111, "arvore_grande"), (1201, 101, "arvore_grande"), (1247, 106, "arvore_grande"), (1297, 114, "arvore_grande"), (1353, 119, "arvore_grande"),
               (509, 135, "arvore_grande"), (741, 126, "arvore_grande"), (847, 122, "arvore_grande"), (896, 134, "arvore_grande"), (811, 143, "arvore_grande"), (1078, 144, "arvore_grande"),
               (1171, 137, "arvore_grande"), (532, 161, "arvore_grande"), (628, 153, "arvore_grande"), (709, 166, "arvore_grande"), (756, 166, "arvore_grande"), (870, 164, "arvore_grande"), 
               (1110, 160, "arvore_grande"), (1273, 159, "arvore_grande"), (657, 184, "arvore_grande"), (928, 180, "arvore_grande"), (1051, 177, "arvore_grande"), (1164, 192, "arvore_grande"), 
               (1221, 173, "arvore_grande"), (1322, 176, "arvore_grande"), (1378, 182, "arvore_grande"), (597, 202, "arvore_grande"), (755, 201, "arvore_grande"),(804, 199, "arvore_grande"), 
               (870, 211, "arvore_grande"),(904, 211, "arvore_grande"),(996, 207, "arvore_grande"),(621, 231, "arvore_grande"),(653, 229, "arvore_grande"),(707, 217, "arvore_grande"),
               (764, 236, "arvore_grande"),(953, 234, "arvore_grande"),(1093, 232, "arvore_grande"),(1344, 237, "arvore_grande"),(897, 260, "arvore_grande"),(625, 278, "arvore_grande"),
               (796, 277, "arvore_grande"),(978, 287, "arvore_grande"),(1065, 268, "arvore_grande"),(1292, 279, "arvore_grande"),(713, 313, "arvore_grande"),(1338, 303, "arvore_grande"),
               (554, 321, "arvore_grande"),(763, 329, "arvore_grande"),(823, 324, "arvore_grande"),(1075, 332, "arvore_grande"),(1277, 326, "arvore_grande"),(645, 344, "arvore_grande"),
               (988, 350, "arvore_grande"),(942, 362, "arvore_grande"),(1142, 350, "arvore_grande"),(1332, 357, "arvore_grande"),(502, 370, "arvore_grande"),(691, 379, "arvore_grande"),
               (887, 381, "arvore_grande"),(1047, 381, "arvore_grande"),(1086, 388, "arvore_grande"),(1179, 376, "arvore_grande"),(1295, 377, "arvore_grande"),(767, 394, "arvore_grande"),
               (849, 396, "arvore_grande"),(1084, 393, "arvore_grande"),(1340, 399, "arvore_grande"),(501, 429, "arvore_grande"),(1307, 415, "arvore_grande"),(540, 449, "arvore_grande"),
               (600, 455, "arvore_grande"),(1340, 442, "arvore_grande"),(892, 463, "arvore_grande"),(952, 480, "arvore_grande"),(508, 494, "arvore_grande"),(566, 495, "arvore_grande"),
               (1377, 489, "arvore_grande"),(932, 527, "arvore_grande"),(530, 537, "arvore_grande"),(603, 536, "arvore_grande"),(507, 596, "arvore_grande"),
               (566, 593, "arvore_grande"),(619, 617, "arvore_grande"),(544, 642, "arvore_grande"),(902, 653, "arvore_grande"),(939, 664, "arvore_grande"),(512, 685, "arvore_grande"),
               (1364, 694, "arvore_grande"),(553, 708, "arvore_grande"),(950, 706, "arvore_grande"),(512, 742, "arvore_grande"),(839, 731, "arvore_grande"),(985, 727, "arvore_grande"),
               (954, 745, "arvore_grande"),(1365, 738, "arvore_grande"),(562, 772, "arvore_grande"),(685, 766, "arvore_grande"),(765, 773, "arvore_grande"),(1013, 768, "arvore_grande"),
               (1337, 763, "arvore_grande"),(817, 780, "arvore_grande"),(975, 781, "arvore_grande"),(1267, 783, "arvore_grande"),(1376, 784, "arvore_grande"),(512, 812, "arvore_grande"),
               (864, 809, "arvore_grande"),(967, 812, "arvore_grande"),(1058, 810, "arvore_grande"),(1165, 809, "arvore_grande"),(1222, 809, "arvore_grande"),(1326, 808, "arvore_grande"),
               (597, 828, "arvore_grande"),(670, 837, "arvore_grande"),(753, 823, "arvore_grande"),(1114, 824, "arvore_grande"),(1361, 834, "arvore_grande"),(537, 851, "arvore_grande"),
               (621, 859, "arvore_grande"),(897, 860, "arvore_grande"),(961, 862, "arvore_grande"),(1022, 857, "arvore_grande"),(1058, 859, "arvore_grande"),(688, 887, "arvore_grande"),
               (1109, 875, "arvore_grande"),(1296, 884, "arvore_grande"),(1349, 877, "arvore_grande"),(774, 904, "arvore_grande"),(918, 914, "arvore_grande"),(1028, 911, "arvore_grande"),
               (1202, 902, "arvore_grande"),(1262, 903, "arvore_grande"),(604, 926, "arvore_grande"),(725, 940, "arvore_grande"),(837, 927, "arvore_grande"),(954, 946, "arvore_grande"),
               (1162, 931, "arvore_grande"),(1350, 931, "arvore_grande"),(1201, 967, "arvore_grande"),(772, 971, "arvore_grande"),(822, 974, "arvore_grande"),(905, 975, "arvore_grande"),
               (1058, 979, "arvore_grande"),(1125, 979, "arvore_grande"),(497, 96, 'arvore_pequena'), (505, 98, 'arvore_pequena'), (511, 96, 'arvore_pequena'), (520, 96, 'arvore_pequena'), (526, 97, 'arvore_pequena'), (535, 97, 'arvore_pequena'), (541, 97, 'arvore_pequena'), (548, 96, 'arvore_pequena'), (553, 96, 'arvore_pequena'), (563, 98, 'arvore_pequena'), (567, 98, 'arvore_pequena'), (619, 97, 'arvore_pequena'), (625, 97, 'arvore_pequena'), (634, 97, 'arvore_pequena'), (640, 98, 'arvore_pequena'), (648, 98, 'arvore_pequena'), (655, 98, 'arvore_pequena'), (659, 96, 'arvore_pequena'), (667, 97, 'arvore_pequena'), (676, 97, 'arvore_pequena'), (680, 96, 'arvore_pequena'), (690, 98, 'arvore_pequena'), (695, 96, 'arvore_pequena'), (702, 96, 'arvore_pequena'), (711, 97, 'arvore_pequena'), (717, 97, 'arvore_pequena'), (722, 97, 'arvore_pequena'), (729, 97, 'arvore_pequena'), (738, 98, 'arvore_pequena'), (746, 97, 'arvore_pequena'), (751, 98, 'arvore_pequena'), (760, 97, 'arvore_pequena'), (765, 97, 'arvore_pequena'), (772, 97, 'arvore_pequena'), (781, 97, 'arvore_pequena'), (785, 96, 'arvore_pequena'), (794, 98, 'arvore_pequena'), (800, 98, 'arvore_pequena'), (806, 97, 'arvore_pequena'), (816, 96, 'arvore_pequena'), (820, 97, 'arvore_pequena'), (828, 98, 'arvore_pequena'), (834, 98, 'arvore_pequena'), (841, 97, 'arvore_pequena'), (848, 96, 'arvore_pequena'), (857, 98, 'arvore_pequena'), (865, 96, 'arvore_pequena'), (869, 98, 'arvore_pequena'), (877, 98, 'arvore_pequena'), (886, 96, 'arvore_pequena'), (892, 97, 'arvore_pequena'), (899, 97, 'arvore_pequena'), (906, 97, 'arvore_pequena'), (914, 96, 'arvore_pequena'), (920, 96, 'arvore_pequena'), (926, 97, 'arvore_pequena'), (933, 96, 'arvore_pequena'), (942, 96, 'arvore_pequena'), (946, 96, 'arvore_pequena'), (954, 98, 'arvore_pequena'), (963, 96, 'arvore_pequena'), (967, 98, 'arvore_pequena'), (976, 97, 'arvore_pequena'), (983, 97, 'arvore_pequena'), (988, 96, 'arvore_pequena'), (996, 98, 'arvore_pequena'), (1005, 98, 'arvore_pequena'), (1009, 98, 'arvore_pequena'), (1017, 98, 'arvore_pequena'), (1024, 98, 'arvore_pequena'), (1031, 96, 'arvore_pequena'), (1038, 96, 'arvore_pequena'), (1047, 98, 'arvore_pequena'), (1052, 97, 'arvore_pequena'), (1059, 96, 'arvore_pequena'), (1067, 98, 'arvore_pequena'), (1074, 98, 'arvore_pequena'), (1080, 97, 'arvore_pequena'), (1089, 96, 'arvore_pequena'), (1094, 97, 'arvore_pequena'), (1101, 97, 'arvore_pequena'), (1108, 96, 'arvore_pequena'), (1116, 96, 'arvore_pequena'), (1121, 98, 'arvore_pequena'), (1131, 98, 'arvore_pequena'), (1138, 97, 'arvore_pequena'), (1145, 96, 'arvore_pequena'), (1152, 97, 'arvore_pequena'), (1159, 96, 'arvore_pequena'), (1166, 96, 'arvore_pequena'), (1170, 96, 'arvore_pequena'), (1178, 97, 'arvore_pequena'), (1184, 96, 'arvore_pequena'), (1193, 98, 'arvore_pequena'), (1200, 96, 'arvore_pequena'), (1207, 96, 'arvore_pequena'), (1215, 96, 'arvore_pequena'), (1219, 97, 'arvore_pequena'), (1228, 97, 'arvore_pequena'), (1236, 98, 'arvore_pequena'), (1242, 97, 'arvore_pequena'), (1249, 98, 'arvore_pequena'), (1255, 96, 'arvore_pequena'), (1263, 96, 'arvore_pequena'), (1268, 96, 
'arvore_pequena'), (1278, 98, 'arvore_pequena'), (1282, 98, 'arvore_pequena'), (1289, 98, 'arvore_pequena'), (1299, 98, 'arvore_pequena'), (1306, 97, 'arvore_pequena'), (1313, 96, 'arvore_pequena'), (1319, 96, 'arvore_pequena'), (1327, 98, 'arvore_pequena'), (1331, 96, 'arvore_pequena'), (1339, 96, 'arvore_pequena'), (1348, 97, 'arvore_pequena'), (1352, 97, 'arvore_pequena'), (1362, 96, 'arvore_pequena'), (1368, 97, 'arvore_pequena'), (1375, 96, 'arvore_pequena'), (499, 102, 'arvore_pequena'), (505, 102, 'arvore_pequena'), (511, 103, 'arvore_pequena'), (520, 103, 'arvore_pequena'), (525, 102, 'arvore_pequena'), (533, 104, 'arvore_pequena'), (539, 103, 'arvore_pequena'), (547, 102, 'arvore_pequena'), (553, 102, 'arvore_pequena'), (560, 104, 'arvore_pequena'), (570, 104, 'arvore_pequena'), (620, 104, 'arvore_pequena'), (624, 103, 'arvore_pequena'), (634, 104, 'arvore_pequena'), (641, 103, 'arvore_pequena'), (646, 104, 'arvore_pequena'), (653, 103, 'arvore_pequena'), (660, 103, 'arvore_pequena'), (667, 104, 'arvore_pequena'), (676, 103, 'arvore_pequena'), (680, 102, 'arvore_pequena'), (688, 103, 'arvore_pequena'), (694, 102, 'arvore_pequena'), (702, 103, 'arvore_pequena'), (710, 102, 'arvore_pequena'), (715, 103, 'arvore_pequena'), (723, 103, 'arvore_pequena'), (730, 102, 'arvore_pequena'), (739, 103, 'arvore_pequena'), (744, 104, 'arvore_pequena'), (751, 102, 'arvore_pequena'), (757, 102, 'arvore_pequena'), (767, 103, 'arvore_pequena'), (773, 102, 'arvore_pequena'), (779, 103, 'arvore_pequena'), (788, 104, 'arvore_pequena'), (794, 104, 'arvore_pequena'), (801, 104, 'arvore_pequena'), (809, 104, 'arvore_pequena'), (814, 104, 'arvore_pequena'), (822, 104, 'arvore_pequena'), (828, 103, 'arvore_pequena'), (837, 102, 'arvore_pequena'), (842, 103, 'arvore_pequena'), (850, 104, 'arvore_pequena'), (857, 102, 'arvore_pequena'), (864, 104, 'arvore_pequena'), (871, 104, 'arvore_pequena'), (877, 102, 'arvore_pequena'), (886, 104, 'arvore_pequena'), (890, 104, 'arvore_pequena'), (898, 104, 'arvore_pequena'), (905, 103, 'arvore_pequena'), (911, 103, 'arvore_pequena'), (918, 102, 'arvore_pequena'), (926, 102, 'arvore_pequena'), (932, 103, 'arvore_pequena'), (940, 104, 
'arvore_pequena'), (947, 104, 'arvore_pequena'), (955, 102, 'arvore_pequena'), (960, 103, 'arvore_pequena'), (967, 104, 'arvore_pequena'), (976, 103, 'arvore_pequena'), (982, 103, 'arvore_pequena'), (989, 102, 'arvore_pequena'), (995, 103, 'arvore_pequena'), (1005, 103, 'arvore_pequena'), (1010, 103, 'arvore_pequena'), (1019, 104, 'arvore_pequena'), (1023, 103, 'arvore_pequena'), (1032, 103, 'arvore_pequena'), (1037, 103, 'arvore_pequena'), (1045, 102, 'arvore_pequena'), (1052, 103, 'arvore_pequena'), (1059, 102, 'arvore_pequena'), (1067, 102, 'arvore_pequena'), (1073, 102, 'arvore_pequena'), (1080, 102, 'arvore_pequena'), (1088, 103, 'arvore_pequena'), (1093, 103, 'arvore_pequena'), (1100, 103, 'arvore_pequena'), (1108, 102, 'arvore_pequena'), (1117, 103, 'arvore_pequena'), (1124, 102, 'arvore_pequena'), (1130, 104, 'arvore_pequena'), (1135, 104, 'arvore_pequena'), (1145, 103, 'arvore_pequena'), (1151, 102, 'arvore_pequena'), (1158, 102, 'arvore_pequena'), (1164, 102, 'arvore_pequena'), (1170, 104, 'arvore_pequena'), (1178, 104, 'arvore_pequena'), (1185, 103, 'arvore_pequena'), (1193, 104, 'arvore_pequena'), (1199, 103, 'arvore_pequena'), (1206, 104, 'arvore_pequena'), (1213, 104, 'arvore_pequena'), (1219, 104, 'arvore_pequena'), (1228, 104, 'arvore_pequena'), (1233, 102, 'arvore_pequena'), (1240, 104, 'arvore_pequena'), (1248, 103, 'arvore_pequena'), (1255, 102, 'arvore_pequena'), (1262, 103, 'arvore_pequena'), (1268, 103, 'arvore_pequena'), (1276, 102, 'arvore_pequena'), (1285, 103, 'arvore_pequena'), (1291, 102, 'arvore_pequena'), (1296, 104, 'arvore_pequena'), (1304, 103, 'arvore_pequena'), (1313, 102, 'arvore_pequena'), (1318, 103, 'arvore_pequena'), (1327, 104, 'arvore_pequena'), (1331, 103, 'arvore_pequena'), (1338, 104, 'arvore_pequena'), (1347, 102, 'arvore_pequena'), (1355, 104, 'arvore_pequena'), (1359, 103, 'arvore_pequena'), (1368, 102, 'arvore_pequena'), (1375, 102, 'arvore_pequena'), (498, 108, 'arvore_pequena'), (504, 110, 'arvore_pequena'), (513, 108, 'arvore_pequena'), (518, 110, 'arvore_pequena'), (525, 108, 'arvore_pequena'), (532, 109, 'arvore_pequena'), (542, 110, 'arvore_pequena'), (549, 108, 'arvore_pequena'), (555, 108, 'arvore_pequena'), (562, 109, 'arvore_pequena'), (570, 108, 'arvore_pequena'), (619, 108, 'arvore_pequena'), (626, 109, 'arvore_pequena'), (632, 109, 'arvore_pequena'), (641, 108, 'arvore_pequena'), (646, 108, 'arvore_pequena'), (654, 108, 'arvore_pequena'), (659, 110, 'arvore_pequena'), (669, 109, 'arvore_pequena'), (674, 110, 'arvore_pequena'), (681, 108, 'arvore_pequena'), (687, 110, 'arvore_pequena'), (694, 109, 'arvore_pequena'), (703, 108, 'arvore_pequena'), (708, 110, 'arvore_pequena'), (715, 109, 'arvore_pequena'), (722, 110, 'arvore_pequena'), (730, 110, 'arvore_pequena'), (739, 110, 'arvore_pequena'), (745, 108, 'arvore_pequena'), (751, 109, 'arvore_pequena'), (759, 108, 'arvore_pequena'), (766, 109, 'arvore_pequena'), (772, 108, 'arvore_pequena'), (778, 109, 'arvore_pequena'), (785, 109, 'arvore_pequena'), (792, 109, 'arvore_pequena'), (801, 110, 'arvore_pequena'), (807, 109, 'arvore_pequena'), (816, 109, 'arvore_pequena'), (822, 110, 'arvore_pequena'), (828, 108, 'arvore_pequena'), (836, 109, 'arvore_pequena'), (843, 109, 'arvore_pequena'), (850, 110, 'arvore_pequena'), (857, 109, 'arvore_pequena'), (863, 108, 'arvore_pequena'), (869, 108, 'arvore_pequena'), (878, 109, 'arvore_pequena'), (885, 109, 'arvore_pequena'), (892, 110, 'arvore_pequena'), (899, 110, 'arvore_pequena'), (906, 108, 
'arvore_pequena'), (914, 108, 'arvore_pequena'), (921, 108, 'arvore_pequena'), (925, 109, 'arvore_pequena'), (934, 110, 'arvore_pequena'), (940, 108, 'arvore_pequena'), (946, 110, 'arvore_pequena'), (953, 108, 'arvore_pequena'), (960, 108, 'arvore_pequena'), (970, 108, 'arvore_pequena'), (976, 110, 'arvore_pequena'), (981, 109, 'arvore_pequena'), (990, 110, 'arvore_pequena'), (996, 110, 'arvore_pequena'), (1002, 110, 'arvore_pequena'), (1012, 109, 'arvore_pequena'), (1016, 109, 'arvore_pequena'), (1025, 110, 'arvore_pequena'), (1033, 109, 'arvore_pequena'), (1039, 110, 'arvore_pequena'), (1044, 110, 'arvore_pequena'), (1051, 108, 'arvore_pequena'), 
(1059, 109, 'arvore_pequena'), (1068, 109, 'arvore_pequena'), (1075, 108, 'arvore_pequena'), (1079, 108, 'arvore_pequena'), (1086, 109, 'arvore_pequena'), (1096, 109, 'arvore_pequena'), (1100, 110, 'arvore_pequena'), (1110, 110, 'arvore_pequena'), (1116, 110, 'arvore_pequena'), (1122, 110, 'arvore_pequena'), (1130, 108, 'arvore_pequena'), (1136, 109, 'arvore_pequena'), (1142, 108, 'arvore_pequena'), (1151, 108, 'arvore_pequena'), (1157, 108, 'arvore_pequena'), (1163, 108, 'arvore_pequena'), (1173, 110, 'arvore_pequena'), (1177, 110, 'arvore_pequena'), (1185, 110, 'arvore_pequena'), (1194, 109, 'arvore_pequena'), (1199, 110, 'arvore_pequena'), (1206, 109, 'arvore_pequena'), (1215, 109, 'arvore_pequena'), (1221, 109, 'arvore_pequena'), (1229, 110, 'arvore_pequena'), (1236, 108, 'arvore_pequena'), (1241, 108, 'arvore_pequena'), (1248, 108, 'arvore_pequena'), (1254, 109, 'arvore_pequena'), (1264, 109, 'arvore_pequena'), (1270, 109, 'arvore_pequena'), (1277, 108, 'arvore_pequena'), (1282, 109, 'arvore_pequena'), (1292, 110, 'arvore_pequena'), (1299, 108, 'arvore_pequena'), (1305, 109, 'arvore_pequena'), (1310, 108, 'arvore_pequena'), (1319, 108, 'arvore_pequena'), (1324, 110, 'arvore_pequena'), (1334, 110, 'arvore_pequena'), (1341, 108, 'arvore_pequena'), (1345, 109, 'arvore_pequena'), (1355, 110, 
'arvore_pequena'), (1362, 110, 'arvore_pequena'), (1366, 108, 'arvore_pequena'), (1373, 110, 'arvore_pequena'), (499, 116, 'arvore_pequena'), (506, 115, 'arvore_pequena'), (512, 114, 'arvore_pequena'), (518, 116, 'arvore_pequena'), (528, 114, 'arvore_pequena'), (533, 116, 'arvore_pequena'), (540, 114, 'arvore_pequena'), (548, 114, 'arvore_pequena'), (554, 115, 'arvore_pequena'), (560, 114, 'arvore_pequena'), (567, 115, 'arvore_pequena'), (620, 116, 'arvore_pequena'), (625, 115, 'arvore_pequena'), (631, 115, 'arvore_pequena'), (640, 115, 'arvore_pequena'), (646, 114, 'arvore_pequena'), (652, 115, 'arvore_pequena'), (662, 116, 'arvore_pequena'), (669, 114, 'arvore_pequena'), (675, 115, 'arvore_pequena'), (681, 115, 'arvore_pequena'), (689, 114, 'arvore_pequena'), (694, 114, 'arvore_pequena'), (704, 114, 'arvore_pequena'), (711, 115, 'arvore_pequena'), (718, 115, 'arvore_pequena'), (724, 114, 'arvore_pequena'), (730, 115, 'arvore_pequena'), (737, 116, 'arvore_pequena'), (745, 115, 'arvore_pequena'), (751, 115, 'arvore_pequena'), (760, 116, 'arvore_pequena'), (766, 114, 'arvore_pequena'), (772, 114, 'arvore_pequena'), (779, 114, 'arvore_pequena'), (788, 115, 'arvore_pequena'), (794, 115, 'arvore_pequena'), (800, 114, 'arvore_pequena'), (806, 116, 'arvore_pequena'), (813, 116, 'arvore_pequena'), (820, 114, 'arvore_pequena'), (829, 114, 'arvore_pequena'), (835, 115, 'arvore_pequena'), (842, 115, 'arvore_pequena'), (850, 115, 'arvore_pequena'), (856, 116, 'arvore_pequena'), (865, 114, 'arvore_pequena'), (871, 116, 
'arvore_pequena'), (876, 115, 'arvore_pequena'), (884, 116, 'arvore_pequena'), (892, 115, 'arvore_pequena'), (897, 114, 'arvore_pequena'), (906, 115, 'arvore_pequena'), (911, 116, 'arvore_pequena'), (920, 115, 'arvore_pequena'), (926, 116, 'arvore_pequena'), (933, 114, 'arvore_pequena'), (942, 114, 'arvore_pequena'), (949, 114, 'arvore_pequena'), (954, 116, 'arvore_pequena'), (963, 114, 'arvore_pequena'), (968, 116, 'arvore_pequena'), (974, 116, 'arvore_pequena'), (981, 114, 'arvore_pequena'), (989, 114, 'arvore_pequena'), (995, 115, 'arvore_pequena'), (1003, 116, 'arvore_pequena'), (1010, 116, 'arvore_pequena'), (1016, 116, 'arvore_pequena'), (1024, 114, 'arvore_pequena'), (1033, 114, 'arvore_pequena'), (1037, 114, 'arvore_pequena'), (1046, 115, 'arvore_pequena'), (1051, 114, 'arvore_pequena'), (1058, 115, 'arvore_pequena'), (1065, 115, 'arvore_pequena'), (1074, 
116, 'arvore_pequena'), (1079, 116, 'arvore_pequena'), (1088, 115, 'arvore_pequena'), (1093, 114, 'arvore_pequena'), (1101, 116, 'arvore_pequena'), (1109, 115, 'arvore_pequena'), (1117, 115, 'arvore_pequena'), (1124, 114, 'arvore_pequena'), (1129, 114, 'arvore_pequena'), (1135, 114, 'arvore_pequena'), (1145, 116, 'arvore_pequena'), (1152, 115, 'arvore_pequena'), (1158, 115, 'arvore_pequena'), (1166, 116, 'arvore_pequena'), (1173, 114, 'arvore_pequena'), (1179, 115, 'arvore_pequena'), (1184, 115, 'arvore_pequena'), (1191, 114, 'arvore_pequena'), (1199, 115, 'arvore_pequena'), (1206, 116, 'arvore_pequena'), (1212, 116, 'arvore_pequena'), (1221, 116, 'arvore_pequena'), (1226, 114, 'arvore_pequena'), (1236, 115, 'arvore_pequena'), (1241, 116, 'arvore_pequena'), (1247, 115, 'arvore_pequena'), (1255, 116, 'arvore_pequena'), (1262, 115, 'arvore_pequena'), (1268, 116, 'arvore_pequena'), (1278, 114, 'arvore_pequena'), (1283, 116, 'arvore_pequena'), (1292, 116, 'arvore_pequena'), (1297, 115, 'arvore_pequena'), (1305, 116, 'arvore_pequena'), (1312, 115, 'arvore_pequena'), (1317, 116, 'arvore_pequena'), (1324, 116, 'arvore_pequena'), (1331, 116, 'arvore_pequena'), (1341, 114, 'arvore_pequena'), (1347, 114, 'arvore_pequena'), (1352, 114, 'arvore_pequena'), (1359, 116, 'arvore_pequena'), (1369, 115, 'arvore_pequena'), (1376, 114, 'arvore_pequena')]


coordenadas.sort(key=lambda x: x[1])
#--------------------------------------------------- ÁRVORES PEQUENAS ---------------------------------------------------------------------------------
    
arvores_pequenas = []

#--------------------------------------------------- ÁRVORES GRANDES ---------------------------------------------------------------------------------

arvores_grandes = []

#--------------------------------------------------- BARRIS ---------------------------------------------------------------------------------

barris = []

#--------------------------------------------------- CASA PEQUENA ---------------------------------------------------------

casas_pequena = []  # Exemplo de posição e tamanho

pach_objects_colision = []

#--------------------------------------------------- TODOS OS OBJETOS COM COLISAO ---------------------------------------------------------------------------------

for x, y, tipo in coordenadas:
    if tipo == "arvore_grande":
        arvores_grandes.append(arvore_grande(x, y, 200 * LArgura // 1920, 60 * LArgura // 1920, arvore_grande_0, -3500, -3500))
        pach_objects_colision.append(arvore_grande(x, y, 200 * LArgura // 1920, 60 * LArgura // 1920, arvore_grande_0, -3500, -3500))
    elif tipo == "arvore_pequena":
        arvores_pequenas.append(arvore_pequena(x, y, 60 * LArgura // 1920, 20 * LArgura // 1920, arvore_pequena_1, -3500, -3500))
        pach_objects_colision.append(arvore_pequena(x, y, 60 * LArgura // 1920, 20 * LArgura // 1920, arvore_pequena_1, -3500, -3500))
    elif tipo == "barril":
        barris.append(barril(x, y, 40 * LArgura // 1920, 15 * LArgura // 1920, barril_0, -3500, -3500))
        pach_objects_colision.append(barril(x, y, 40 * LArgura // 1920, 15 * LArgura // 1920, barril_0, -3500, -3500))
    elif tipo == "casa_pequena":
        casa_pequena.append(casa_pequena(x, y, 243 * LArgura // 1920, 90 * LArgura // 1920, casa_pequena0, -3500, -3500))
        pach_objects_colision.append(casa_pequena(x, y, 243 * LArgura // 1920, 90 * LArgura // 1920, casa_pequena0, -3500, -3500))



arvores_pequenas_rects = [arvore.rect() for arvore in arvores_pequenas]

arvores_grandes_rects = [arvore.rect() for arvore in arvores_grandes]

barris_rects = [barril.rect() for barril in barris]

casas_pequena_rect = [casa.rect() for casa in casas_pequena]

pach_objects_colision = barris + arvores_pequenas + arvores_grandes + casas_pequena
pach_objects_rects_colision = arvores_pequenas_rects + arvores_grandes_rects + barris_rects + casas_pequena_rect

#--------------------------------------------------- COM LENTIDAO ---------------------------------------------------------------------------------

class arbusto:
    def __init__(self, x, y, largura, altura, imagem_pach, pos_chao_x, pos_chao_y):
        self.x = x * LArgura // 1920
        self.y = y * LArgura // 1920
        self.pos_chao_x = pos_chao_x
        self.pos_chao_y = pos_chao_y
        self.largura =  largura * LArgura // 1920
        self.altura = altura * LArgura // 1920
        self.imagem_pach = imagem_pach
        self.bottom_left = 48
        self.bottom_rith = 30
    
    def rect(self):
        """Retorna um pygame.Rect para usar na colisão"""
        return pygame.Rect(0 + (((self.x - 500) * 19200) // (1380 - 500) + self.pos_chao_x),
                            0 + (((self.y - 100) * 19200) // (980 - 100) + self.pos_chao_y),
                            48 * LArgura // 1920, 48 * LArgura // 1920)
    
#--------------------------------------------------- ARBUSTOS ---------------------------------------------------------------------------------

arbustos = [arbusto(350, 250, 50, 50, arbusto_0, -3500, -3500),
            arbusto(750, 350, 50, 50, arbusto_1, -3500, -3500),
            arbusto(550, 450, 50, 50, arbusto_2, -3500, -3500),
            arbusto(950, 250, 50, 50, arbusto_3, -3500, -3500)]

arbustos_rects = [arbusto.rect() for arbusto in arbustos]

#--------------------------------------------------- TODOS OS OBJETOS COM LENTIDAO ---------------------------------------------------------------------------------

pach_objects_colision_lentidao = arbustos
pach_objects_rects_colision_lentidao = arbustos_rects

#--------------------------------------------------- Sem interação ---------------------------------------------------------------------------------

class cogumelo:
    def __init__(self, x, y, largura, altura, imagem_pach):
        self.x = x * LArgura // 1920
        self.y = y * LArgura // 1920
        self.largura =  largura * LArgura // 1920
        self.altura = altura * LArgura // 1920
        self.imagem_pach = imagem_pach

class pedra:
    def __init__(self, x, y, largura, altura, imagem_pach):
        self.x = x * LArgura // 1920
        self.y = y * LArgura // 1920
        self.largura =  largura * LArgura // 1920
        self.altura = altura * LArgura // 1920
        self.imagem_pach = imagem_pach

#--------------------------------------------------- COGUMELOS ---------------------------------------------------------------------------------

cogumelos = [cogumelo(450, 150, 50, 50, cogumelo_0)]

#--------------------------------------------------- PEDRAS ---------------------------------------------------------------------------------

pedras = [pedra(250, 350, 50, 50, pedras_0),
          pedra(850, 400, 50, 50, pedras_1),
          pedra(1050, 200, 50, 50, pedras_2),
          pedra(1050, 40, 50, 50, pedras_3)]

#--------------------------------------------------- TODOS OS OBJETOS SEM INTERAÇÃO ---------------------------------------------------------------------------------

pach_objects_sem_interação = cogumelos + pedras

#--------------------------------------------------- TODOS OS OBJETOS DO CENÁRIO ---------------------------------------------------------------------------------

pach_objects = pach_objects_colision_lentidao + pach_objects_colision
pach_objects_intamgible = pach_objects_sem_interação

class GerenciadorDeColisao:
    def __init__(self, arvores_pequenas, arvores_grandes, barris, casas_pequenas, arbustos, cogumelos, pedras):
        self.arvores_pequenas = arvores_pequenas
        self.arvores_grandes = arvores_grandes
        self.barris = barris
        self.arbustos = arbustos
        self.cogumelos = cogumelos
        self.pedras = pedras
        self.casas_pequenas = casas_pequenas

        self.objetos_colisao = []
        self.objetos_lentidao = []
        self.objetos_sem_interacao = []
        self.todos_objetos = []

    def atualizar(self, pos_chao_x, pos_chao_y):
        """Atualiza listas de objetos a cada frame"""
        self.objetos_colisao = self.arvores_pequenas + self.arvores_grandes + self.barris + self.casas_pequenas
        self.objetos_lentidao = self.arbustos
        self.objetos_sem_interacao = self.cogumelos + self.pedras
        self.todos_objetos = self.objetos_sem_interacao + self.objetos_lentidao + self.objetos_colisao

    def colide(self, rect, pos_chao_x, pos_chao_y):
        """Verifica colisão com objetos sólidos"""
        return any(rect.colliderect((((obj.x - 500) * 19200) // (1380 - 500) + pos_chao_x) + obj.bottom_rith,
                                         (((obj.y - 100) * 19200) // (980 - 100) + pos_chao_y) + obj.bottom_left,
                                         obj.largura, obj.altura) for obj in self.objetos_colisao)

    def colide_lentidao(self, rect):
        """Verifica colisão com objetos que reduzem velocidade"""
        return any(rect.colliderect(obj.rect()) for obj in self.objetos_lentidao)
    
gerenciador_colisao = GerenciadorDeColisao(arvores_pequenas, arvores_grandes, barris, casas_pequena ,arbustos, cogumelos, pedras)
gerenciador_colisao.atualizar(-3500, -3500)