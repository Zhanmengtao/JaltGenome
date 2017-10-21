#!/usr/bin/env python
"""
remove species due to bad gene annotations 
remove potential gene isoforms based on geneid
Example: python remove_redundancy.py -i mclOutput -s obtusifolia annuum
"""
import argparse


def remove_isoforms(cluster):
	geneids = cluster.split('\t')
	loci = [x.split('.')[0] for x in geneids]
	updated_ids = list(set(loci))
	if len(updated_ids) != len(geneids):
		print cluster
	output = '\t'.join(updated_ids)
	return output

		
def filter_data(infile, species):
	outfile = open("updated_MCLout", "w")
	with open("mclOutput", "r") as infile:
		for line in infile:
			line = line.rstrip()
			updated_ids = remove_isoforms(line)
			if any(item in updated_ids for item in species):
				mylist = updated_ids.split()
				data = ''
				for x in xrange(len(mylist)):
					if any(item in mylist[x] for item in species):
						pass
					elif data == '':
						data = mylist[x]
					else:
						data += '\t'+mylist[x]
				if data != '':
					outfile.write(data+'\n')
			else:
				outfile.write(updated_ids+'\n')
			
			


def main():
	parser = argparse.ArgumentParser(prog="remove_redundancy.py", description=__doc__,
	formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('-i', '--infile', \
	help=("the output generated by orthoMCL"), required=True)
	parser.add_argument('-s', '--species', \
	help=("species need to be removed"), nargs='*',required=True)
	args = parser.parse_args()
	
	infile = args.infile
	species = list(args.species)
		
	filter_data(infile,species)


if __name__ == "__main__":
	main()