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
        self.bottom_left = 170
        self.bottom_rith = 43
        self.altura_real =210
        self.largura_real =158
    
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
        self.altura_real =360
        self.largura_real =256
    
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
        self.altura_real =65
        self.largura_real =40
    
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
        self.altura_real =450
        self.largura_real =288
    
    def rect(self):
        """Retorna um pygame.Rect para usar na colisão"""
        return pygame.Rect(20 * LArgura // 1920 + (((self.x - 500) * 19200) // (1380 - 500) + self.pos_chao_x),
                            170 * LArgura // 1920 + (((self.y - 100) * 19200) // (980 - 100) + self.pos_chao_y),
                              243 * LArgura // 1920, 90 * LArgura // 1920)

coordenadas = [(534, 107, "arvore_grande"), (632, 101, "arvore_grande"), (804, 101, "arvore_grande"), (940, 104, "arvore_grande"), (1042, 101, "arvore_grande"),
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
               (1058, 979, "arvore_grande"),(1125, 979, "arvore_grande"),(500, 95, 'arvore_pequena'), (509, 95, 'arvore_pequena'), (517, 94, 'arvore_pequena'), (523, 96, 'arvore_pequena'), (536, 96, 'arvore_pequena'), (542, 94, 'arvore_pequena'), (553, 93, 'arvore_pequena'), (561, 95, 'arvore_pequena'), (572, 95, 'arvore_pequena'), (624, 94, 'arvore_pequena'), (632, 94, 'arvore_pequena'), (643, 94, 'arvore_pequena'), (650, 93, 'arvore_pequena'), (658, 96, 'arvore_pequena'), (669, 93, 'arvore_pequena'), (678, 95, 'arvore_pequena'), (685, 93, 'arvore_pequena'), (696, 94, 'arvore_pequena'), (706, 96, 'arvore_pequena'), (711, 96, 'arvore_pequena'), (722, 95, 'arvore_pequena'), (729, 96, 'arvore_pequena'), (738, 93, 'arvore_pequena'), (749, 95, 'arvore_pequena'), (757, 93, 'arvore_pequena'), (768, 94, 'arvore_pequena'), (775, 94, 'arvore_pequena'), (786, 96, 'arvore_pequena'), (793, 93, 'arvore_pequena'), (805, 94, 'arvore_pequena'), (812, 94, 'arvore_pequena'), (820, 94, 'arvore_pequena'), (832, 95, 'arvore_pequena'), (841, 94, 'arvore_pequena'), (849, 95, 'arvore_pequena'), (857, 93, 'arvore_pequena'), (864, 95, 'arvore_pequena'), (873, 94, 'arvore_pequena'), (884, 95, 'arvore_pequena'), (892, 94, 'arvore_pequena'), (904, 93, 'arvore_pequena'), (910, 94, 'arvore_pequena'), (918, 96, 'arvore_pequena'), (927, 93, 'arvore_pequena'), (940, 93, 'arvore_pequena'), (945, 96, 'arvore_pequena'), (955, 96, 'arvore_pequena'), (966, 94, 'arvore_pequena'), (972, 93, 'arvore_pequena'), (985, 94, 'arvore_pequena'), (991, 93, 'arvore_pequena'), (999, 95, 'arvore_pequena'), (1012, 95, 'arvore_pequena'), (1021, 93, 'arvore_pequena'), (1026, 93, 'arvore_pequena'), (1036, 94, 'arvore_pequena'), (1045, 93, 'arvore_pequena'), (1053, 93, 'arvore_pequena'), (1064, 94, 'arvore_pequena'), (1072, 96, 'arvore_pequena'), (1084, 93, 'arvore_pequena'), (1093, 93, 'arvore_pequena'), (1100, 93, 'arvore_pequena'), (1111, 94, 'arvore_pequena'), (1120, 95, 'arvore_pequena'), (1125, 93, 'arvore_pequena'), (1136, 94, 'arvore_pequena'), (1143, 94, 'arvore_pequena'), (1153, 95, 'arvore_pequena'), (1161, 95, 'arvore_pequena'), (1170, 96, 'arvore_pequena'), (1180, 94, 'arvore_pequena'), (1191, 94, 'arvore_pequena'), (1200, 96, 'arvore_pequena'), (1207, 96, 'arvore_pequena'), (1219, 95, 'arvore_pequena'), (1227, 94, 'arvore_pequena'), (1233, 93, 'arvore_pequena'), (1244, 96, 'arvore_pequena'), (1255, 94, 'arvore_pequena'), (1262, 95, 'arvore_pequena'), (1272, 95, 'arvore_pequena'), (1282, 95, 'arvore_pequena'), (1291, 94, 'arvore_pequena'), (1299, 93, 'arvore_pequena'), (1309, 93, 'arvore_pequena'), (1315, 94, 'arvore_pequena'), (1325, 93, 'arvore_pequena'), (1334, 94, 'arvore_pequena'), (1344, 96, 'arvore_pequena'), (1350, 95, 'arvore_pequena'), (1361, 94, 'arvore_pequena'), (1372, 93, 'arvore_pequena'), (500, 105, 'arvore_pequena'), (505, 105, 'arvore_pequena'), (518, 103, 'arvore_pequena'), (524, 102, 'arvore_pequena'), (536, 104, 'arvore_pequena'), (544, 105, 'arvore_pequena'), (551, 103, 'arvore_pequena'), (561, 104, 'arvore_pequena'), (568, 105, 'arvore_pequena'), (624, 103, 'arvore_pequena'), (633, 104, 'arvore_pequena'), (641, 102, 'arvore_pequena'), (649, 102, 'arvore_pequena'), (658, 102, 'arvore_pequena'), (667, 105, 'arvore_pequena'), (678, 102, 'arvore_pequena'), (685, 105, 'arvore_pequena'), (696, 104, 'arvore_pequena'), (706, 103, 'arvore_pequena'), (712, 105, 'arvore_pequena'), (724, 105, 'arvore_pequena'), (733, 105, 'arvore_pequena'), (742, 103, 'arvore_pequena'), (747, 104, 'arvore_pequena'), (756, 104, 'arvore_pequena'), (766, 104, 'arvore_pequena'), (774, 105, 'arvore_pequena'), (786, 103, 'arvore_pequena'), (796, 103, 'arvore_pequena'), (803, 105, 'arvore_pequena'), (812, 102, 'arvore_pequena'), (820, 103, 'arvore_pequena'), (829, 102, 'arvore_pequena'), (841, 102, 'arvore_pequena'), (849, 102, 'arvore_pequena'), (856, 104, 'arvore_pequena'), (867, 105, 'arvore_pequena'), (876, 105, 'arvore_pequena'), (886, 105, 'arvore_pequena'), (893, 104, 'arvore_pequena'), (902, 104, 'arvore_pequena'), (910, 103, 'arvore_pequena'), (921, 102, 'arvore_pequena'), (927, 102, 'arvore_pequena'), (938, 105, 'arvore_pequena'), (948, 102, 'arvore_pequena'), (955, 105, 'arvore_pequena'), (963, 102, 'arvore_pequena'), (974, 105, 'arvore_pequena'), (982, 103, 'arvore_pequena'), (992, 103, 'arvore_pequena'), (1000, 105, 'arvore_pequena'), (1010, 102, 'arvore_pequena'), (1017, 103, 'arvore_pequena'), (1030, 102, 'arvore_pequena'), (1035, 102, 'arvore_pequena'), (1045, 103, 'arvore_pequena'), (1056, 105, 'arvore_pequena'), (1063, 105, 'arvore_pequena'), (1074, 103, 'arvore_pequena'), (1081, 104, 'arvore_pequena'), (1091, 104, 'arvore_pequena'), (1098, 104, 'arvore_pequena'), (1109, 103, 'arvore_pequena'), (1119, 105, 'arvore_pequena'), (1128, 102, 'arvore_pequena'), (1136, 102, 'arvore_pequena'), (1145, 102, 'arvore_pequena'), (1152, 103, 'arvore_pequena'), (1161, 104, 'arvore_pequena'), (1173, 102, 'arvore_pequena'), (1181, 104, 'arvore_pequena'), (1188, 103, 'arvore_pequena'), (1201, 102, 'arvore_pequena'), (1208, 104, 'arvore_pequena'), (1217, 103, 'arvore_pequena'), (1226, 104, 'arvore_pequena'), (1236, 105, 'arvore_pequena'), (1246, 103, 'arvore_pequena'), (1251, 104, 'arvore_pequena'), (1260, 104, 'arvore_pequena'), (1272, 102, 'arvore_pequena'), (1279, 105, 'arvore_pequena'), (1291, 104, 'arvore_pequena'), (1300, 105, 'arvore_pequena'), (1307, 102, 'arvore_pequena'), (1318, 104, 'arvore_pequena'), (1324, 104, 'arvore_pequena'), (1332, 104, 'arvore_pequena'), (1343, 104, 'arvore_pequena'), (1354, 102, 'arvore_pequena'), (1359, 104, 'arvore_pequena'), (1368, 104, 'arvore_pequena'), (499, 112, 'arvore_pequena'), (508, 113, 'arvore_pequena'), (515, 114, 'arvore_pequena'), (526, 111, 'arvore_pequena'), (533, 112, 'arvore_pequena'), (545, 114, 'arvore_pequena'), (551, 114, 'arvore_pequena'), (561, 111, 'arvore_pequena'), (572, 112, 'arvore_pequena'), (625, 113, 'arvore_pequena'), (630, 113, 'arvore_pequena'), (643, 112, 'arvore_pequena'), (651, 111, 'arvore_pequena'), (661, 114, 'arvore_pequena'), (670, 114, 'arvore_pequena'), (679, 112, 'arvore_pequena'), (688, 113, 'arvore_pequena'), (696, 111, 'arvore_pequena'), (702, 114, 'arvore_pequena'), (714, 111, 'arvore_pequena'), (720, 113, 'arvore_pequena'), (732, 113, 'arvore_pequena'), (742, 112, 'arvore_pequena'), (749, 114, 'arvore_pequena'), (759, 112, 'arvore_pequena'), (769, 113, 'arvore_pequena'), (777, 113, 'arvore_pequena'), (787, 113, 'arvore_pequena'), (796, 114, 'arvore_pequena'), (804, 113, 'arvore_pequena'), (811, 111, 'arvore_pequena'), (819, 112, 'arvore_pequena'), (832, 111, 'arvore_pequena'), (839, 112, 'arvore_pequena'), (846, 111, 'arvore_pequena'), (859, 113, 'arvore_pequena'), (865, 111, 'arvore_pequena'), (877, 111, 'arvore_pequena'), (883, 114, 'arvore_pequena'), (893, 112, 'arvore_pequena'), (904, 111, 'arvore_pequena'), (909, 113, 'arvore_pequena'), (921, 113, 'arvore_pequena'), (929, 111, 'arvore_pequena'), (939, 113, 'arvore_pequena'), (948, 114, 'arvore_pequena'), (956, 111, 'arvore_pequena'), (966, 114, 'arvore_pequena'), (976, 112, 'arvore_pequena'), (985, 114, 'arvore_pequena'), (994, 112, 'arvore_pequena'), (1002, 113, 'arvore_pequena'), (1011, 114, 'arvore_pequena'), (1020, 114, 'arvore_pequena'), (1028, 114, 'arvore_pequena'), (1037, 111, 'arvore_pequena'), (1046, 111, 'arvore_pequena'), (1053, 112, 'arvore_pequena'), (1064, 111, 'arvore_pequena'), (1072, 112, 'arvore_pequena'), (1081, 111, 'arvore_pequena'), (1089, 112, 'arvore_pequena'), (1098, 111, 'arvore_pequena'), (1107, 114, 'arvore_pequena'), (1119, 111, 'arvore_pequena'), (1127, 114, 'arvore_pequena'), (1135, 113, 'arvore_pequena'), (1147, 113, 'arvore_pequena'), (1152, 111, 'arvore_pequena'), (1164, 111, 'arvore_pequena'), (1172, 112, 'arvore_pequena'), (1182, 114, 'arvore_pequena'), (1189, 114, 'arvore_pequena'), (1197, 113, 'arvore_pequena'), (1206, 113, 'arvore_pequena'), (1218, 111, 'arvore_pequena'), (1227, 114, 'arvore_pequena'), (1236, 113, 'arvore_pequena'), (1245, 114, 'arvore_pequena'), (1251, 114, 'arvore_pequena'), (1264, 111, 'arvore_pequena'), (1272, 114, 'arvore_pequena'), (1280, 114, 'arvore_pequena'), (1291, 113, 'arvore_pequena'), (1299, 113, 'arvore_pequena'), (1309, 114, 'arvore_pequena'), (1315, 112, 'arvore_pequena'), (1323, 113, 'arvore_pequena'), (1332, 114, 'arvore_pequena'), (1343, 112, 'arvore_pequena'), (1353, 114, 'arvore_pequena'), (1359, 114, 'arvore_pequena'), (1369, 112, 'arvore_pequena'),
               (497, 122, 'arvore_pequena'), (509, 121, 'arvore_pequena'), (516, 120, 'arvore_pequena'), (525, 122, 'arvore_pequena'), (535, 122, 'arvore_pequena'), (541, 123, 'arvore_pequena'), (552, 120, 'arvore_pequena'), (561, 120, 'arvore_pequena'), (677, 120, 'arvore_pequena'), (686, 122, 'arvore_pequena'), (696, 122, 'arvore_pequena'), (702, 121, 'arvore_pequena'), (714, 122, 'arvore_pequena'), (721, 123, 'arvore_pequena'), (731, 121, 'arvore_pequena'), (740, 123, 'arvore_pequena'), (748, 123, 'arvore_pequena'), (760, 123, 'arvore_pequena'), (769, 123, 'arvore_pequena'), (774, 123, 'arvore_pequena'), (787, 120, 'arvore_pequena'), (793, 121, 'arvore_pequena'), (803, 123, 'arvore_pequena'), (814, 120, 'arvore_pequena'), (822, 121, 'arvore_pequena'), (831, 121, 'arvore_pequena'), (837, 123, 'arvore_pequena'), (846, 120, 'arvore_pequena'), (856, 122, 'arvore_pequena'), (867, 120, 'arvore_pequena'), (875, 120, 'arvore_pequena'), (885, 123, 'arvore_pequena'), (894, 123, 'arvore_pequena'), (904, 123, 'arvore_pequena'), (909, 122, 'arvore_pequena'), (918, 120, 'arvore_pequena'), (927, 121, 'arvore_pequena'), (940, 121, 'arvore_pequena'), (947, 123, 'arvore_pequena'), (957, 120, 'arvore_pequena'), (964, 120, 'arvore_pequena'), (972, 123, 'arvore_pequena'), (984, 122, 'arvore_pequena'), (990, 121, 'arvore_pequena'), (1001, 120, 'arvore_pequena'), (1009, 123, 'arvore_pequena'), (1020, 120, 'arvore_pequena'), (1028, 120, 'arvore_pequena'), (1037, 120, 'arvore_pequena'), (1047, 120, 'arvore_pequena'), (1057, 120, 'arvore_pequena'), (1066, 123, 'arvore_pequena'), (1071, 122, 'arvore_pequena'), (1084, 121, 'arvore_pequena'), (1091, 121, 'arvore_pequena'), (1099, 122, 'arvore_pequena'), (1110, 121, 'arvore_pequena'), (1118, 120, 'arvore_pequena'), (1126, 122, 'arvore_pequena'), (1137, 122, 'arvore_pequena'), (1143, 120, 'arvore_pequena'), (1153, 122, 'arvore_pequena'), (1162, 121, 'arvore_pequena'), (1173, 120, 'arvore_pequena'), (1179, 123, 'arvore_pequena'), (1188, 120, 'arvore_pequena'), (1197, 120, 'arvore_pequena'), (1206, 120, 'arvore_pequena'), (1216, 123, 'arvore_pequena'), (1227, 120, 'arvore_pequena'), (1237, 120, 'arvore_pequena'), (1245, 121, 'arvore_pequena'), (1252, 121, 'arvore_pequena'), (1262, 123, 'arvore_pequena'), (1270, 120, 'arvore_pequena'), (1280, 121, 'arvore_pequena'), (1288, 120, 'arvore_pequena'), (1296, 122, 'arvore_pequena'), (1309, 120, 'arvore_pequena'), (1314, 120, 'arvore_pequena'), (1324, 120, 'arvore_pequena'), (1336, 123, 'arvore_pequena'), (1345, 120, 'arvore_pequena'), (1350, 121, 'arvore_pequena'), (1361, 120, 'arvore_pequena'), (1368, 123, 'arvore_pequena'),(499, 132, 'arvore_pequena'), (507, 131, 'arvore_pequena'), (517, 129, 'arvore_pequena'), (526, 132, 'arvore_pequena'), (536, 129, 'arvore_pequena'), (541, 132, 'arvore_pequena'), (554, 130, 'arvore_pequena'), (673, 130, 'arvore_pequena'), (685, 130, 'arvore_pequena'), (693, 129, 'arvore_pequena'), (703, 129, 'arvore_pequena'), (709, 129, 'arvore_pequena'), (717, 129, 'arvore_pequena'), (726, 130, 'arvore_pequena'), (736, 130, 'arvore_pequena'), (746, 129, 'arvore_pequena'), (757, 130, 'arvore_pequena'), (764, 132, 'arvore_pequena'), (773, 129, 'arvore_pequena'), (784, 129, 'arvore_pequena'), (793, 129, 'arvore_pequena'), (798, 132, 'arvore_pequena'), (807, 129, 'arvore_pequena'), (818, 129, 'arvore_pequena'), (826, 132, 'arvore_pequena'), (837, 130, 'arvore_pequena'), (843, 129, 'arvore_pequena'), (855, 131, 'arvore_pequena'), (862, 132, 'arvore_pequena'), (871, 129, 'arvore_pequena'), (879, 129, 'arvore_pequena'), (889, 131, 'arvore_pequena'), (898, 131, 'arvore_pequena'), (909, 129, 'arvore_pequena'), (916, 130, 'arvore_pequena'), (928, 131, 'arvore_pequena'), (936, 131, 'arvore_pequena'), (943, 132, 'arvore_pequena'), (954, 132, 'arvore_pequena'), (960, 132, 'arvore_pequena'), (972, 131, 'arvore_pequena'), (978, 130, 'arvore_pequena'), (991, 130, 'arvore_pequena'), (997, 131, 'arvore_pequena'), (1009, 131, 'arvore_pequena'), (1016, 129, 'arvore_pequena'), (1024, 129, 'arvore_pequena'), 
               (1036, 130, 'arvore_pequena'), (1042, 130, 'arvore_pequena'), (1052, 129, 'arvore_pequena'), (1059, 129, 'arvore_pequena'), (1068, 131, 'arvore_pequena'), (1078, 130, 'arvore_pequena'), (1087, 129, 'arvore_pequena'), (1098, 129, 'arvore_pequena'), (1106, 130, 'arvore_pequena'), (1115, 132, 'arvore_pequena'), (1123, 131, 'arvore_pequena'), (1133, 131, 'arvore_pequena'), (1141, 130, 'arvore_pequena'), (1152, 131, 'arvore_pequena'), (1162, 129, 'arvore_pequena'), (1171, 129, 'arvore_pequena'), (1180, 132, 'arvore_pequena'), (1189, 129, 'arvore_pequena'), (1194, 129, 'arvore_pequena'), (1207, 130, 'arvore_pequena'), (1216, 129, 'arvore_pequena'), (1225, 129, 'arvore_pequena'), (1233, 130, 'arvore_pequena'), (1241, 131, 'arvore_pequena'), (1251, 131, 'arvore_pequena'), (1257, 130, 'arvore_pequena'), (1270, 130, 'arvore_pequena'), (1276, 132, 'arvore_pequena'), (1284, 131, 'arvore_pequena'), (1295, 131, 'arvore_pequena'), (1303, 131, 'arvore_pequena'), (1313, 129, 'arvore_pequena'), (1320, 132, 'arvore_pequena'), (1331, 130, 'arvore_pequena'), (1341, 132, 'arvore_pequena'), (1349, 129, 'arvore_pequena'), (1359, 131, 'arvore_pequena'), (1368, 129, 'arvore_pequena'), (1378, 131, 'arvore_pequena'),
               (498, 138, 'arvore_pequena'), (507, 141, 'arvore_pequena'), (514, 139, 'arvore_pequena'), (526, 139, 'arvore_pequena'), (535, 139, 'arvore_pequena'), (544, 138, 'arvore_pequena'), (551, 141, 'arvore_pequena'), (673, 138, 'arvore_pequena'), (679, 141, 'arvore_pequena'), (689, 139, 'arvore_pequena'), (700, 141, 'arvore_pequena'), (709, 140, 'arvore_pequena'), (715, 140, 'arvore_pequena'), (724, 138, 'arvore_pequena'), (736, 141, 'arvore_pequena'), (742, 139, 'arvore_pequena'), (753, 141, 'arvore_pequena'), (761, 140, 'arvore_pequena'), (771, 140, 'arvore_pequena'), (777, 141, 'arvore_pequena'), (788, 139, 'arvore_pequena'), (799, 141, 'arvore_pequena'), (806, 141, 'arvore_pequena'), (815, 138, 'arvore_pequena'), (824, 139, 'arvore_pequena'), (834, 140, 'arvore_pequena'), (842, 140, 'arvore_pequena'), (853, 138, 'arvore_pequena'), (860, 138, 'arvore_pequena'), (868, 140, 'arvore_pequena'), (877, 141, 'arvore_pequena'), (887, 141, 'arvore_pequena'), (895, 141, 'arvore_pequena'), (905, 138, 'arvore_pequena'), (915, 140, 'arvore_pequena'), (922, 141, 'arvore_pequena'), (934, 138, 'arvore_pequena'), (941, 141, 'arvore_pequena'), (948, 140, 'arvore_pequena'), (961, 139, 'arvore_pequena'), (966, 141, 'arvore_pequena'), (977, 141, 'arvore_pequena'), (984, 138, 'arvore_pequena'), (996, 140, 'arvore_pequena'), (1002, 141, 'arvore_pequena'), (1013, 140, 'arvore_pequena'), (1024, 138, 'arvore_pequena'), (1032, 139, 'arvore_pequena'), (1038, 139, 'arvore_pequena'), (1050, 139, 'arvore_pequena'), (1056, 140, 'arvore_pequena'), (1067, 141, 'arvore_pequena'), (1076, 139, 'arvore_pequena'), (1085, 140, 'arvore_pequena'), (1093, 138, 'arvore_pequena'), (1104, 138, 'arvore_pequena'), (1110, 140, 'arvore_pequena'), (1119, 140, 'arvore_pequena'), (1130, 139, 'arvore_pequena'), (1137, 139, 'arvore_pequena'), (1146, 140, 'arvore_pequena'), (1159, 140, 'arvore_pequena'), (1165, 141, 'arvore_pequena'), (1175, 138, 'arvore_pequena'), (1184, 138, 'arvore_pequena'), (1195, 139, 'arvore_pequena'), (1201, 140, 'arvore_pequena'), (1212, 138, 'arvore_pequena'), (1219, 138, 'arvore_pequena'), (1229, 138, 'arvore_pequena'), (1236, 141, 'arvore_pequena'), (1245, 141, 'arvore_pequena'), (1254, 140, 'arvore_pequena'), (1263, 141, 'arvore_pequena'), (1273, 141, 'arvore_pequena'), (1282, 138, 'arvore_pequena'), (1293, 141, 'arvore_pequena'), (1301, 140, 'arvore_pequena'), (1308, 138, 'arvore_pequena'), (1321, 141, 'arvore_pequena'), (1328, 141, 'arvore_pequena'), (1337, 138, 'arvore_pequena'), (1346, 138, 'arvore_pequena'), (1354, 138, 'arvore_pequena'), (1363, 141, 'arvore_pequena'), (1375, 140, 'arvore_pequena')
               ]


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
        arvores_pequenas.append(arvore_pequena(x, y, 70 * LArgura // 1920, 33 * LArgura // 1920, arvore_pequena_2, -3500, -3500))
        pach_objects_colision.append(arvore_pequena(x, y, 70 * LArgura // 1920, 33 * LArgura // 1920, arvore_pequena_2, -3500, -3500))
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
        self.altura_real =60
        self.largura_real =60
    
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