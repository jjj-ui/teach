#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�2020/11/23
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ��
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name == 'ʯͷ':
        return 0

    elif name == 'ʷ����':
        return 1

    elif name == '��':
        return 2

    elif name == '����':
        return 3

    elif name == '����':
        return 4

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


    #��дִ�д���,������ɺ�passɾ��


def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number in range(0,5):
        if number==0:
            return 'ʯͷ'

        elif number==1:
            return 'ʷ����'

        elif number==2:
            return '��'

        elif number==3:
            return '����'

        elif number==4:
            return '����'


    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

    #��дִ�д���,������ɺ�passɾ��


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    print('����ѡ��Ϊ:',player_choice)
    player_number=name_to_number(player_choice)
    comp_number=random.randrange(0,5)
    comp_choice=number_to_name(comp_number)
    print('�������ѡ��Ϊ��',comp_choice)
    if player_number-comp_number==-4 or player_number-comp_number==-3 or player_number-comp_number==1 or player_number-comp_number==2:
        print('��Ӯ��!')
    elif player_number-comp_number==-2 or player_number-comp_number==-1 or player_number-comp_number==3 or player_number-comp_number==4:
        print('�����Ӯ��!')
    elif player_number-comp_number==0:
        print('���ͼ��������һ����!')

    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

    #����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
if  choice_name=='ʯͷ' or choice_name=='ʷ����' or choice_name=='��' or choice_name=='����' or choice_name=='����':
    rpsls(choice_name)
else:
    print('Error: No Correct Name')



